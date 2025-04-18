from django.urls import path
from . import views
from .views import register_view

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', register_view, name='register'),
    path('signup/', views.signup_view, name='signup'),
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
    path('senior_manager/', views.senior_manager_view, name='senior_manager'),
    path('engineer/', views.engineer_view, name='engineer'),
    path('team_leader/', views.team_leader_view, name='team_leader'),
    path('department_leader/', views.department_leader_view, name='department_leader'),
    path('admin/', views.admin_login_view, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('user_management/', views.user_management_view, name='user_management'),
    path('team_management/', views.team_management_view, name='team_management'),
    path('session_management/', views.session_management_view, name='session_management'),
    path('department_management/', views.department_management_view, name='department_management'),
     path('card_management/', views.card_management_view, name='card_management'),
]