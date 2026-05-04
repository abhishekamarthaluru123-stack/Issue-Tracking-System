from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ⭐ THIS FIXES YOUR ERROR
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('BugReportingSystem/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_bug, name='create_bug'),
    path('assign/<int:pk>/', views.assign_bug, name='assign_bug'),
    path('update/<int:pk>/', views.update_status, name='update_status'),
    path('logout/', views.user_logout, name='logout'),
]