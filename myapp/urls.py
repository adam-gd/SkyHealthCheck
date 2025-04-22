from django.urls import path
from . import views
from .views import register_view

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('password-reset/', views.change_password, name='password_reset'),  # Placeholder for password reset
    # Engineer URLs
    path('engineer-dashboard/', views.engineer_dashboard, name='engineer_dashboard'),
    path('vote-session/', views.vote_session, name='vote_session'),
    path('team-summary/', views.view_team_summary, name='team_summary'),
    # Team Leader URLs
    path('team-leader-dashboard/', views.team_leader_dashboard, name='team_leader_dashboard'),
    path('team-cards/', views.view_team_cards, name='team_cards'),
    # Department Leader URLs
    path('department-leader-dashboard/', views.department_leader_dashboard, name='department_leader_dashboard'),
    path('department-summary/', views.view_department_summary, name='department_summary'),
    # Senior Manager URLs
    path('senior-manager-dashboard/', views.senior_manager_dashboard, name='senior_manager_dashboard'),
    path('all-summaries/', views.view_all_summaries, name='all_summaries'),
    # Existing URLs
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