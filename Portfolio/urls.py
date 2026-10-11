from django.urls import path
from . import views

urlpatterns = [
   
    # Public Pages
    path('', views.home, name='home'),
    path('portfolio/', views.Portfolio, name='portfolio'),
    path('resume/', views.resume_view, name='resume'),
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Profile
    path('profile/update/', views.update_profile, name='update_profile'),
    path('change-pass/', views.change_pass, name='change_pass'),

    # Skill Management
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/create/', views.skill_create, name='skill_create'),
    path('skills/update/<int:id>/', views.skill_update, name='skill_update'),
    path('skills/delete/<int:id>/', views.skill_delete, name='skill_delete'),

    # Education Management
    path('education/', views.education_list, name='education_list'),
    path('education/create/', views.education_create, name='education_create'),
    path('education/update/<int:id>/', views.education_update, name='education_update'),
    path('education/delete/<int:id>/', views.education_delete, name='education_delete'),

    # Experience Management
    path('experience/', views.experience_list, name='experience_list'),
    path('experience/create/', views.experience_create, name='experience_create'),
    path('experience/update/<int:id>/', views.experience_update, name='experience_update'),
    path('experience/delete/<int:id>/', views.experience_delete, name='experience_delete'),

    # Project Management
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/update/<int:id>/', views.project_update, name='project_update'),
    path('projects/delete/<int:id>/', views.project_delete, name='project_delete'),

    # Contact Messages
    path('contact/messages/', views.contact_messages, name='contact_messages'),
    path('contact/messages/<int:id>/', views.contact_message_detail, name='contact_message_detail'),
    path('contact/messages/<int:id>/delete/', views.contact_message_delete, name='contact_message_delete'),



    # Main Manage Portfolio Page
    # path(
    #     'manage-portfolio/',
    #     views.manage_portfolio,
    #     name='manage_portfolio'
    # ),



]
