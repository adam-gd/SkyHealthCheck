from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Department, Team, HealthCard, Session, CustomUser, Vote

# Branding the admin site
admin.site.site_header = "MyApp Admin"
admin.site.site_title  = "MyApp Administration"
admin.site.index_title = "Dashboard Overview"

# Register Department
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display  = ('name', 'leader')  # Added 'leader' to display the department leader
    search_fields = ('name',)
    list_filter   = ('leader',)

# Register Team
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display  = ('name', 'department', 'leader')  # Added 'leader' to display the team leader
    list_filter   = ('department', 'leader')
    search_fields = ('name',)

# Register HealthCard
@admin.register(HealthCard)
class HealthCardAdmin(admin.ModelAdmin):
    list_display  = ('title',)  # Reverted to 'title' (this matches your original admin.py)
    search_fields = ('title',)

# Register Session
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display  = ('name', 'start_date', 'end_date')
    list_filter   = ('start_date', 'end_date')
    search_fields = ('name',)

# Register Vote
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display  = ('user', 'session', 'card', 'team', 'vote', 'progress', 'created_at')
    list_filter   = ('vote', 'progress', 'session', 'team')
    search_fields = ('user__username', 'card__title')  # Updated to use 'card__title'

# Register CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'team', 'is_staff']  # Added 'team'
    list_filter = ['role', 'team']
    search_fields = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)