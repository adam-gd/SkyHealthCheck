from django.contrib import admin
from .models import Department, Team, HealthCard, Session
from .models import CustomUser

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)

@admin.register(HealthCard)
class HealthCardAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    
    

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)