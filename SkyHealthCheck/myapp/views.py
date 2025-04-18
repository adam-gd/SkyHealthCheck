from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm
from django.contrib import messages
from django.http import Http404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Or wherever you want
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    return render(request, 'myapp/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard_view(request):
    role = request.user.role
    if role == 'engineer':
        return render(request, 'dashboards/engineer.html')
    elif role == 'team_leader':
        return render(request, 'dashboards/team_leader.html')
    elif role == 'department_leader':
        return render(request, 'dashboards/department_leader.html')
    elif role == 'senior_manager':
        return render(request, 'dashboards/senior_manager.html')
    return render(request, 'dashboards/default.html')


def delivering_value_view(request):
    return render(request, 'cards/delivering_value.html')

def easy_to_release_view(request):
    return render(request, 'cards/easy_to_release.html')

def fun_view(request):
    return render(request, 'cards/fun.html')

def learning_view(request):
    return render(request, 'cards/learning.html')

def mission_view(request):
    return render(request, 'cards/mission.html')

def speed_view(request):
    return render(request, 'cards/speed.html')

def support_view(request):
    return render(request, 'cards/support.html')

def teamwork_view(request):
    return render(request, 'cards/teamwork.html')


def overview_view(request):
    return render(request, 'overview.html')

def agreements_view(request):
    return render(request, 'agreements.html')

def home_view(request):
    return render(request, 'home.html')

def sky_vote_view(request):
    return render(request, 'sky_vote.html')

def senior_manager_view(request):
    return render(request, 'senior_manager.html')

def engineer_view(request):
    return render(request, 'engineer.html')

def team_leader_view(request):
    return render(request, 'team_leader.html')

def department_leader_view(request):
    return render(request, 'department_leader.html')

def admin_login_view(request):
    return render(request, 'admin_login.html')

def admin_dashboard_view(request):
    return render(request, 'admin/admin_dashboard.html')

def user_management_view(request):
    return render(request, 'admin/user_management.html')


def team_management_view(request):
    return render(request, 'admin/team_management.html')


def session_management_view(request):
    return render(request, 'admin/session_management.html')

def department_management_view(request):
    return render(request, 'admin/department_management.html')

def card_management_view(request):
    return render(request, 'admin/card_management.html')