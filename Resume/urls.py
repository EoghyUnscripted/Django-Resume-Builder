from django.urls import path, include

from . import views

urlpatterns = [
    # Employers
    path('employer/', views.employer, name='employer'),
    # Universities
    path('university/', views.university, name='university'),
    # Skills
    path('skill/<int:skill_id>/', views.skill_details, name='skill'),
    # Applications
    path('app/<int:app_id>/', views.app, name='app'),
    path('plain/<int:app_id>/', views.plain, name='plain'),
    path('cov/<int:app_id>/', views.cover, name='cover'),
]
