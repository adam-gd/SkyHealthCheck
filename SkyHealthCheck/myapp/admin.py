from django.contrib import admin
from .models import Department, Team, HealthCard, Session
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Branding the admin site
admin.site.site_header = "MyApp Admin"
admin.site.site_title  = "MyApp Administration"
admin.site.index_title = "Dashboard Overview"

# Register Department
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display  = ('name',)
    search_fields = ('name',)

# Register Team
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display  = ('name', 'department')
    list_filter   = ('department',)
    search_fields = ('name',)

# Register HealthCard
@admin.register(HealthCard)
class HealthCardAdmin(admin.ModelAdmin):
    list_display  = ('title',)
    search_fields = ('title',)

# Register Session
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display  = ('name', 'start_date', 'end_date')
    list_filter   = ('start_date', 'end_date')
    search_fields = ('name',)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
