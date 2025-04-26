from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from .forms import CustomUserCreationForm, RegisterForm, LoginForm
from .models import CustomUser, Team, HealthCard, Vote, Department

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
    return render(request, 'myapp/register.html', {'form': form})

# Login page (unchanged)
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
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
    return render(request, 'myapp/login.html', {'form': form})

# Logout view (unchanged)
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

# Role-based access control decorator (unchanged)
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

# Updated signup view to use RegisterForm by AFTAB (unchanged)
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
            return render(request, 'myapp/signup_success.html')
    else:
        form = RegisterForm()
    return render(request, 'myapp/signup.html', {'form': form})

# Dashboard view (updated for role-based redirection) (unchanged)
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
    return render(request, 'myapp/dashboard.html')

# Search view for team leader dashboard (unchanged)
@role_required('team_leader')
def search_view(request):
    query = request.GET.get('q', '')
    teams = Team.objects.filter(name__icontains=query, leader=request.user)
    cards = HealthCard.objects.filter(title__icontains=query)
    context = {
        'query': query,
        'teams': teams,
        'cards': cards,
    }
    return render(request, 'myapp/search_results.html', context)

# Engineer-specific views (unchanged)
@role_required('engineer')
def engineer_dashboard(request):
    return render(request, 'myapp/engineer.html')

@role_required('engineer')
def vote_session(request):
    return render(request, 'myapp/vote_session.html')

@role_required('engineer')
def view_team_summary(request):
    return render(request, 'myapp/team_summary.html')

# Team Leader-specific views (unchanged)
@role_required('team_leader')
def team_leader_dashboard(request):
    user = request.user
    try:
        team = Team.objects.get(leader=user)
        teams = Team.objects.filter(department=team.department)
        cards = HealthCard.objects.all()
        votes = Vote.objects.filter(team=team).select_related('card')
        progress_summary = {}
        for card in cards:
            card_votes = votes.filter(card=card)
            if card_votes.exists():
                vote_counts = {
                    'green': card_votes.filter(vote='green').count(),
                    'amber': card_votes.filter(vote='amber').count(),
                    'red': card_votes.filter(vote='red').count(),
                }
                progress_summary[card.title] = vote_counts
        other_departments = Department.objects.exclude(id=team.department.id)
        dept_progress = {}
        for dept in other_departments:
            dept_votes = Vote.objects.filter(team__department=dept).select_related('card')
            dept_summary = {}
            for card in cards:
                card_votes = dept_votes.filter(card=card)
                if card_votes.exists():
                    vote_counts = {
                        'green': card_votes.filter(vote='green').count(),
                        'amber': card_votes.filter(vote='amber').count(),
                        'red': card_votes.filter(vote='red').count(),
                    }
                    dept_summary[card.title] = vote_counts
            dept_progress[dept.name] = dept_summary
        context = {
            'team': team,
            'teams': teams,
            'cards': cards,
            'progress_summary': progress_summary,
            'dept_progress': dept_progress,
        }
    except Team.DoesNotExist:
        messages.error(request, 'You are not assigned as a leader to any team.')
        context = {}
    return render(request, 'myapp/team_leader.html', context)

@role_required('team_leader')
def view_team_cards(request):
    user = request.user
    try:
        team = Team.objects.get(leader=user)
        teams = Team.objects.filter(department=team.department)
        cards = HealthCard.objects.all()
        context = {'team': team, 'teams': teams, 'cards': cards}
    except Team.DoesNotExist:
        messages.error(request, 'You are not assigned as a leader to any team.')
        context = {}
    return render(request, 'myapp/team_cards.html', context)

@role_required('team_leader')
def view_cards_progress(request):
    user = request.user
    try:
        team = Team.objects.get(leader=user)
        cards = HealthCard.objects.all()
        votes = Vote.objects.filter(team=team).select_related('card')
        progress_summary = {}
        for card in cards:
            card_votes = votes.filter(card=card)
            if card_votes.exists():
                vote_counts = {
                    'green': card_votes.filter(vote='green').count(),
                    'amber': card_votes.filter(vote='amber').count(),
                    'red': card_votes.filter(vote='red').count(),
                }
                progress_summary[card.title] = vote_counts
        context = {'team': team, 'progress_summary': progress_summary}
    except Team.DoesNotExist:
        messages.error(request, 'You are not assigned as a leader to any team.')
        context = {}
    return render(request, 'myapp/cards_progress.html', context)

@role_required('team_leader')
def view_other_department_progress(request):
    user = request.user
    try:
        team = Team.objects.get(leader=user)
        other_departments = Department.objects.exclude(id=team.department.id)
        cards = HealthCard.objects.all()
        dept_progress = {}
        for dept in other_departments:
            dept_votes = Vote.objects.filter(team__department=dept).select_related('card')
            dept_summary = {}
            for card in cards:
                card_votes = dept_votes.filter(card=card)
                if card_votes.exists():
                    vote_counts = {
                        'green': card_votes.filter(vote='green').count(),
                        'amber': card_votes.filter(vote='amber').count(),
                        'red': card_votes.filter(vote='red').count(),
                    }
                    dept_summary[card.title] = vote_counts
            dept_progress[dept.name] = dept_summary
        context = {'dept_progress': dept_progress}
    except Team.DoesNotExist:
        messages.error(request, 'You are not assigned as a leader to any team.')
        context = {}
    return render(request, 'myapp/other_department_progress.html', context)

# Department Leader-specific views (unchanged)
@role_required('department_leader')
def department_leader_dashboard(request):
    return render(request, 'myapp/department_leader.html')

@role_required('department_leader')
def view_department_summary(request):
    return render(request, 'myapp/department_summary.html')

# Senior Manager-specific views (unchanged)
@role_required('senior_manager')
def senior_manager_dashboard(request):
    return render(request, 'myapp/senior_manager.html')

@role_required('senior_manager')
def view_all_summaries(request):
    return render(request, 'myapp/all_summaries.html')

# Profile update view (unchanged)
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
    return render(request, 'myapp/update_profile.html')

# Updated change_password view for Reset Password page
@login_required
def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password and confirm_password:
            if new_password == confirm_password:
                user = request.user
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password changed successfully! Please log in again.')
                logout(request)  # Log out after password change
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match.')
        else:
            messages.error(request, 'Please fill in both password fields.')
    return render(request, 'myapp/change_password.html')

# Other views (unchanged)
def delivering_value_view(request):
    return render(request, 'myapp/cards/delivering_value.html')

def easy_to_release_view(request):
    return render(request, 'myapp/cards/easy_to_release.html')

def fun_view(request):
    return render(request, 'myapp/cards/fun.html')

def learning_view(request):
    return render(request, 'myapp/cards/learning.html')

def mission_view(request):
    return render(request, 'myapp/cards/mission.html')

def speed_view(request):
    return render(request, 'myapp/cards/speed.html')

def support_view(request):
    return render(request, 'myapp/cards/support.html')

def teamwork_view(request):
    return render(request, 'myapp/cards/teamwork.html')

def overview_view(request):
    return render(request, 'myapp/overview.html')

def agreements_view(request):
    return render(request, 'myapp/agreements.html')

def home_view(request):
    return render(request, 'myapp/home.html')

def sky_vote_view(request):
    return render(request, 'myapp/sky_vote.html')

def senior_manager_view(request):
    return render(request, 'myapp/senior_manager.html')

def engineer_view(request):
    return render(request, 'myapp/engineer.html')

def team_leader_view(request):
    return render(request, 'myapp/team_leader.html')

def department_leader_view(request):
    return render(request, 'myapp/department_leader.html')

def admin_login_view(request):
    return render(request, 'myapp/admin_login.html')

def admin_dashboard_view(request):
    return render(request, 'myapp/admin/admin_dashboard.html')

def user_management_view(request):
    return render(request, 'myapp/admin/user_management.html')

def team_management_view(request):
    return render(request, 'myapp/admin/team_management.html')

def session_management_view(request):
    return render(request, 'myapp/admin/session_management.html')

def department_management_view(request):
    return render(request, 'myapp/admin/department_management.html')

def card_management_view(request):
    return render(request, 'myapp/admin/card_management.html')