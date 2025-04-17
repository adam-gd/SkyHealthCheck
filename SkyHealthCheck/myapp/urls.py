from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
     path('delivering_value/', views.delivering_value_view, name='delivering_value'),
    path('easy_to_release/', views.easy_to_release_view, name='easy_to_release'),
    path('agreements/', views.agreements_view, name='agreements'),
     path('home/', views.home_view, name='home'),
    path('sky_vote/', views.sky_vote_view, name='sky_vote'),
    path('overview/', views.overview_view, name='overview'),
    path('senior_manager/', views.senior_manager_view, name='senior_manager'),
    path('engineer/', views.engineer_view, name='engineer'),
    path('team_leader/', views.team_leader_view, name='team_leader'),
    path('department_leader/', views.department_leader_view, name='department_leader'),
    path('admin/', views.admin_login_view, name='admin_login'),
]