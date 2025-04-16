from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

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
