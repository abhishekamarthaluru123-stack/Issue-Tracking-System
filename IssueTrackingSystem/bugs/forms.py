from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Bug

ROLE_CHOICES = [
    ('Manager', 'Manager'),
    ('Developer', 'Developer'),
    ('Tester', 'Tester'),
]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=ROLE_CHOICES)

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AssignForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['assigned_to']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(groups__name='Developer')