from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # or wherever
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def role_required(role):
    def check(user):
        return user.role == role
    return user_passes_test(check)

@login_required
@role_required('team_leader')
def team_leader_dashboard(request):
    return render(request, 'team_leader_dashboard.html')