from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.Acceuil, name='Acceuil'), 
    path('contact/', views.Contact, name='contact'), 
    path('job-details/', views.jobdetails, name='job-details'), 
    path('job-listings/', views.joblistings, name='job-listings'), 
    path('about/', views.about, name='about')
]
