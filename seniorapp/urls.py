from django.urls import path 
from . import views
urlpatterns = [
    # path('', views.login, name='login' ) ,
    path('contact.html', views.contact, name='contact' ) ,
    path('services.html', views.services, name='services' ), 
    path('companies.html', views.companies, name='companies' ), 
    path('profile.html', views.profile, name='profile' ), 
    path('studentregistration.html', views.studentregistration, name='studentregistration' ), 
    path('Reportsubmission.html', views.Reportsubmission, name='Reportsubmission' ), 
    path('Tracking.html', views.Tracking, name='Tracking' ), 
    path('Recommendation.html', views.Recommendation, name='Recommendation' ),
    path('coordinatorEv.html', views.coordinatorEv, name='coordinatorEv' ),
    path('Traineelist.html', views.Traineelist, name='Traineelist' ),
    path('Traineedetails.html', views.Traineedetails, name='Traineedetails' ),
    path('Addcompanies.html', views.Addcompanies, name='Addcompanies' ),
    path('companydetails.html', views.companydetails, name='companydetails' ),
    path('submitCV.html', views.submitCV, name='submitCV' ),
    path('companyregistration.html', views.companyregistration, name='companyregistration' ),
    path('companyprofile.html', views.companyprofile, name='companyprofile' ),
    path('superevisorevaluation.html', views.superevisorevaluation, name='superevisorevaluation' ),
    path('Register.html', views.Register, name='Register' ),
    path('TryTemplate.html', views.TryTemplate, name='TryTemplate' ),
    path('Request.html', views.Request, name='Request' ),
    path('register_test', views.register_test, name='register_test' ),
    path('', views.home_test, name='home' ),
    path('test_login', views.test_login, name='login' ),
    path('test_logout', views.test_logout, name='logout' ),
]