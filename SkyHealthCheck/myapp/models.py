from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.
# myapp/models.py
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class HealthCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Session(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    
    
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('engineer', 'Engineer'),
        ('team_leader', 'Team Leader'),
        ('department_leader', 'Department Leader'),
        ('senior_manager', 'Senior Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='engineer')
    pass 

class Card(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name