from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render (request ,'seniorapp\login.html')

def contact(request):
    return render (request ,'seniorapp\contact.html')

def services(request):
    return render (request ,'seniorapp\services.html')    


def companies(request):
    return render (request ,'seniorapp\companies.html')    

def profile(request):
    return render (request ,'seniorapp\profile.html')     

def studentregistration(request):
    return render (request ,'seniorapp\studentregistration.html')    

def Reportsubmission(request):
    return render (request ,'seniorapp\Reportsubmission.html') 

def Tracking(request):
    return render (request ,'seniorapp\Tracking.html')    

def Recommendation(request):
    return render (request ,'seniorapp\Recommendation.html')   

def coordinatorEv(request):
    return render (request ,'seniorapp\coordinatorEv.html')           

def Traineelist(request):
    return render (request ,'seniorapp\Traineelist.html')     

def Traineedetails(request):
    return render (request ,'seniorapp\Traineedetails.html')           


def Addcompanies(request):
    return render (request ,'seniorapp\Addcompanies.html')   

def companydetails(request):
    return render (request ,'seniorapp\companydetails.html')      

def submitCV(request):
    return render (request ,'seniorapp\submitCV.html')   

def companyregistration(request):
    return render (request ,'seniorapp\companyregistration.html')       

def companyprofile(request):
    return render (request ,'seniorapp\companyprofile.html')   

def superevisorevaluation(request):
    return render (request ,'seniorapp\superevisorevaluation.html')   

def Register(request):
    return render (request ,'seniorapp\Register.html') 

def TryTemplate(request):
    return render (request ,'seniorapp\TryTemplate.html')                              