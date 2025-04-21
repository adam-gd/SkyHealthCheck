from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegisterForm
from django.contrib import messages
from django.http import Http404
from .models import CustomUser, Department, Team, HealthCard, Session, Card
from django.utils import timezone

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
            return redirect('login')  
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

def vote_view(request):
    return render(request, 'vote/vote.html')

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
    add_message = ''
    delete_message = ''

    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST.get('username')
            if username:
                CustomUser.objects.create(username=username)
                add_message = f"User '{username}' added successfully!"
        elif 'delete_username' in request.POST:
            user_id = request.POST.get('delete_username')
            user = get_object_or_404(CustomUser, id=user_id)
            username = user.username
            user.delete()
            delete_message = f"User '{username}' deleted successfully!"

    users = CustomUser.objects.all()
    return render(request, 'admin/user_management.html', {
        'add_message': add_message,
        'delete_message': delete_message,
        'users': users
    })



def team_management_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            team_name     = request.POST.get('team_name')
            department_id = request.POST.get('department_id')
            if team_name and department_id:
                department = get_object_or_404(Department, id=department_id)
                Team.objects.create(name=team_name, department=department)
                messages.success(request, f"Team '{team_name}' added successfully!")
            else:
                messages.error(request, "You must choose a department and enter a team name.")

        elif action == 'delete':
            team_id = request.POST.get('team_id')
            if team_id:
                team = get_object_or_404(Team, id=team_id)
                team_name = team.name
                team.delete()
                messages.error(request, f"Team '{team_name}' deleted successfully!")
            else:
                messages.error(request, "You must select a team to delete.")

        # Redirect to the same page so that the browser’s refresh won’t re‑POST
        return redirect('team_management')  
        # (Make sure you have this name in your urls.py: path('teams/', team_management_view, name='team_management'))

    # GET
    return render(request, 'admin/team_management.html', {
        'departments': Department.objects.all(),
        'teams':       Team.objects.all(),
    })


def session_management_view(request):
    message = ''
    message_color = 'green'  
    if request.method == 'POST':
        action = request.POST.get('action')

        # Add session
        if action == 'add':
            session_name = request.POST.get('session_name')
            if session_name:
                start_date = timezone.now() 
                end_date = timezone.now() + timezone.timedelta(hours=1)
                Session.objects.create(name=session_name)
                message = f"Session '{session_name}' added successfully!"
                message_color = 'green'

        # Delete session
        elif action == 'delete':
            session_id = request.POST.get('delete_session_id')
            if session_id:
                try:
                    session = Session.objects.get(id=session_id)
                    session.delete()
                    message = f"Session '{session.name}' deleted successfully!"
                    message_color = 'red'
                except Session.DoesNotExist:
                    message = "Session not found."
                    message_color = 'red'

    # Fetch all sessions to display in the dropdown
    sessions = Session.objects.all()
    return render(request, 'admin/session_management.html', {
        'message': message,
        'message_color': message_color,
        'sessions': sessions
    })

def department_management_view(request):
    message = ''
    message_color = 'green'  # Default to green

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            dept_name = request.POST.get('department_name')
            if dept_name:
                Department.objects.create(name=dept_name)
                message = f"Department '{dept_name}' added successfully!"
                message_color = 'green'

        elif action == 'delete':
            dept_id = request.POST.get('delete_department_id')
            if dept_id:
                try:
                    dept = Department.objects.get(id=dept_id)
                    dept.delete()
                    message = f"Department '{dept.name}' deleted successfully!"
                    message_color = 'red'
                except Department.DoesNotExist:
                    message = "Department not found."
                    message_color = 'red'

    departments = Department.objects.all()
    return render(request, 'admin/department_management.html', {
        'message': message,
        'message_color': message_color,
        'departments': departments
    })
    
    
def card_management_view(request):
    message = ''  # Initialize message variable
    message_color = ''  # Initialize the color variable for the message

    # Add Card
    if request.method == 'POST' and 'add_card' in request.POST:
        card_name = request.POST.get('card_name')  # Get card name from form
        if card_name:
            # Check if the card already exists in the database
            if Card.objects.filter(name=card_name).exists():
                message = f"Card '{card_name}' already exists!"  # Error message
                message_color = 'red'  # Show error message in red
            else:
                # Create the card if it doesn't exist
                Card.objects.create(name=card_name)
                message = f"Card '{card_name}' added successfully!"  # Success message
                message_color = 'green'  # Success message in green

    # Delete Card
    elif request.method == 'POST' and 'delete_card' in request.POST:
        card_id = request.POST.get('card_id')  # Get card ID from the delete dropdown
        if card_id:
            try:
                card = Card.objects.get(id=card_id)
                card_name = card.name  # Save the name before deletion
                card.delete()  # Delete the selected card
                message = f"Card '{card_name}' deleted successfully!"  # Success message
                message_color = 'red'  # Red color for deleted cards
            except Card.DoesNotExist:
                message = "Card not found!"  # Error message if card doesn't exist
                message_color = 'red'  # Error message in red

    # Fetch all cards for the dropdown
    cards = Card.objects.all()

    return render(request, 'admin/card_management.html', {'message': message, 'message_color': message_color, 'cards': cards})


def view_departments(request):
    departments = Department.objects.all()
    return render(request, 'admin/view_departments.html', {'departments': departments})

def view_teams(request):
    teams = Team.objects.all()
    return render(request, 'admin/view_teams.html', {'teams': teams})

def view_users(request):
    users = CustomUser.objects.all()
    return render(request, 'admin/view_users.html', {'users': users})

def view_cards(request):
    cards = HealthCard.objects.all()
    return render(request, 'admin/view_cards.html', {'cards': cards})


def view_sessions(request):
    sessions = Session.objects.select_related('created_by').all()
    return render(request, 'admin/view_sessions.html', {'sessions': sessions})
