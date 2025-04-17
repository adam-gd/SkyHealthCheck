from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


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
    return render(request, 'delivering_value.html')

def easy_to_release_view(request):
    return render(request, 'easy_to_release.html')

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