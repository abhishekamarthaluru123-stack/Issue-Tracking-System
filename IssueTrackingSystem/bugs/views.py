from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Bug
from .forms import LoginForm, BugForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


from django.contrib import messages

def user_login(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = authenticate(request, username=username, password=password)

            if user is None:
                messages.error(request, "Invalid username or password.")
            elif not user.groups.filter(name=role).exists():
                messages.error(request, "You selected the wrong role.")
            else:
                login(request, user)
                return redirect('dashboard')

    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    status_filter = request.GET.get('status')
    search_query = request.GET.get('search')

    bugs = Bug.objects.all()

    if status_filter and status_filter != "All":
        bugs = bugs.filter(status=status_filter)

    if search_query:
        bugs = bugs.filter(title__icontains=search_query)

    return render(request, 'dashboard.html', {
        'bugs': bugs,
        'search_query': search_query
    })


@login_required
def create_bug(request):
    if request.user.groups.filter(name='Tester').exists():
        form = BugForm(request.POST or None)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.created_by = request.user
            bug.save()
            return redirect('dashboard')
        return render(request, 'create_bug.html', {'form': form})
    return redirect('dashboard')


@login_required
def assign_bug(request, pk):
    if request.user.groups.filter(name='Manager').exists():

        bug = get_object_or_404(Bug, pk=pk)
        developers = User.objects.filter(groups__name='Developer')

        if request.method == "POST":
            dev_id = request.POST.get('developer')
            bug.assigned_to = User.objects.get(id=dev_id)
            bug.save()
            return redirect('dashboard')

        return render(request, 'assign.html', {
            'bug': bug,
            'developers': developers
        })

    return redirect('dashboard')


@login_required
def update_status(request, pk):
    bug = get_object_or_404(Bug, pk=pk)

    if request.user == bug.assigned_to:
        bug.status = "Resolved"
        bug.save()

    return redirect('dashboard')


def user_logout(request):
    logout(request)
    return redirect('home')