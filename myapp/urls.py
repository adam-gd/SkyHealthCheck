from django.urls import path
from . import views
from .views import register_view

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin/', views.admin_login_view, name='admin_login'),
    path('admin_login/', views.admin_login_view, name='admin_login'),
    path('admin_signup/', views.admin_signup_view, name='admin_signup'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('engineer_login/', views.engineer_login_view, name='engineer_login'),
    path('Dleader_login/', views.Dleader_login_view, name='Dleader_login'),
     path('team_leader/', views.team_leader_view, name='team_leader'),
    path('senior_manager/', views.senior_manager_view, name='senior_manager'),
      
    path(
      'senior_manager/signup/',
      views.senior_manager_signup,
      name='senior_manager_signup'
    ),
    path(
      'team_leader/signup/',
      views.team_leader_signup,
      name='team_leader_signup'
    ),
    path(
      'department_leader/signup/',
      views.department_leader_signup,
      name='department_leader_signup'
    ),
    path('register/', register_view, name='register'),
    path('engineer_signup/', views.engineer_signup_view, name='engineer_signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('delivering_value/', views.delivering_value_view, name='delivering_value'),
    path('easy_to_release/', views.easy_to_release_view, name='easy_to_release'),
    path('fun/', views.fun_view, name='fun'),
    path('learning/', views.learning_view, name='learning'),
    path('mission/', views.mission_view, name='mission'),
    path('speed/', views.speed_view, name='speed'),
    path('support/', views.support_view, name='support'),
    path('teamwork/', views.teamwork_view, name='teamwork'),
    path('agreements/', views.agreements_view, name='agreements'),
    path('home/', views.home_view, name='home'),
    path('sky_vote/', views.sky_vote_view, name='sky_vote'),
    path('overview/', views.overview_view, name='overview'),
    path('engineer/', views.engineer_view, name='engineer'),
    path('user_management/', views.user_management_view, name='user_management'),
    path('team_management/', views.team_management_view, name='team_management'),
    path('session_management/', views.session_management_view, name='session_management'),
    path('department_management/', views.department_management_view, name='department_management'),
    path('card_management/', views.card_management_view, name='card_management'),
    path('departments/', views.view_departments, name='view_departments'),
    path('teams/', views.view_teams, name='view_teams'),
    path('sessions/', views.view_sessions, name='view_sessions'),
    path('users/', views.view_users, name='view_users'),
    path('cards/', views.view_cards, name='view_cards'),
    path('vote/', views.vote_view, name='vote'), ]