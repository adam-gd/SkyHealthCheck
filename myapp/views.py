from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from .forms import CustomUserCreationForm, RegisterForm, LoginForm
from .models import CustomUser

# Register view (unchanged)
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login page
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Authenticate user using email
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                # Redirect based on role
                if user.role == 'engineer':
                    return redirect('engineer_dashboard')
                elif user.role == 'team_leader':
                    return redirect('team_leader_dashboard')
                elif user.role == 'department_leader':
                    return redirect('department_leader_dashboard')
                elif user.role == 'senior_manager':
                    return redirect('senior_manager_dashboard')
                else:
                    return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

# Role-based access control decorator
def role_required(*roles):
    def decorator(view_func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.role in roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'You do not have permission to access this page.')
                return redirect('dashboard')
        return wrapper
    return decorator

# Updated signup view to use RegisterForm by AFTAB
def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                role='engineer'  # Default role for signup
            )
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return render(request, 'signup_success.html')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

# Dashboard view (updated for role-based redirection)
@login_required
def dashboard_view(request):
    if request.user.role == 'engineer':
        return redirect('engineer_dashboard')
    elif request.user.role == 'team_leader':
        return redirect('team_leader_dashboard')
    elif request.user.role == 'department_leader':
        return redirect('department_leader_dashboard')
    elif request.user.role == 'senior_manager':
        return redirect('senior_manager_dashboard')
    return render(request, 'dashboard.html')

# Engineer-specific views
@role_required('engineer')
def engineer_dashboard(request):
    return render(request, 'engineer.html')

@role_required('engineer')
def vote_session(request):
    # Placeholder for voting on health cards
    return render(request, 'vote_session.html')

@role_required('engineer')
def view_team_summary(request):
    # Placeholder for viewing team summaries
    return render(request, 'team_summary.html')

# Team Leader-specific views
@role_required('team_leader')
def team_leader_dashboard(request):
    return render(request, 'team_leader.html')

@role_required('team_leader')
def view_team_cards(request):
    # Placeholder for viewing team cards
    return render(request, 'team_cards.html')

# Department Leader-specific views
@role_required('department_leader')
def department_leader_dashboard(request):
    return render(request, 'department_leader.html')

@role_required('department_leader')
def view_department_summary(request):
    # Placeholder for viewing department summaries
    return render(request, 'department_summary.html')

# Senior Manager-specific views
@role_required('senior_manager')
def senior_manager_dashboard(request):
    return render(request, 'senior_manager.html')

@role_required('senior_manager')
def view_all_summaries(request):
    # Placeholder for viewing all summaries
    return render(request, 'all_summaries.html')

# Profile update view
@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('dashboard')
    return render(request, 'update_profile.html')

# Password change view (placeholder)
@login_required
def change_password(request):
    # Implement password change logic using Django's built-in views if needed
    return render(request, 'change_password.html')

# Other views (unchanged)
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