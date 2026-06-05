from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact/send/', views.send_contact_email, name='send_contact_email'),
    path('download-resume/', views.download_resume, name='download_resume'),
]
