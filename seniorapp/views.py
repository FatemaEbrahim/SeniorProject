import time
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentCreationForm, StudentLoginForm
from .models import Student
# from django.contrib.auth import logout
from .custom_auth import StudentAuthBackend
# from .forms import NameForm

# Create your views here.

def _login(request):
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

def home_test(request):
    return render (request ,'seniorapp\\home_test.html')   

def Request(request):
    return render (request ,'seniorapp\\Request.html')

def register_test(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentCreationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return StudentCreationForm('/thanks/')
            student = Student.objects.create_user(
                academic_id = request.POST['academic_id'],
                name = request.POST['name'],
                cpr = request.POST['cpr'],
                gpa = request.POST['gpa'],
                college = request.POST['college'],
                department = request.POST['department'],
                course = request.POST['course'],
                password = request.POST['password1']
            )
            username = request.POST['student_id']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                logged_in = True
                ...
            else:
                # Return an 'invalid login' error message.
                ...
                    # student.login
            return render (request ,'seniorapp\\register_test.html', {'form': form, 'student':student, 'logged_in':logged_in})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentCreationForm()
    return render (request ,'seniorapp\\register_test.html', {'form': form})

def test_login(request):
    if request.method == 'POST':
        username = request.POST['academic_id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        time.sleep(2)
        return redirect('home')

        pass
    else:
        # username = '20152340'
        # password = 'qwaszxerdfcv'
        form = StudentLoginForm(initial={'academic_id': '20152340', 'password':'qwaszxerdfcv'})
        pass
    return render (request ,'seniorapp\\test_login.html', {'user':request.user, 'form':form})

def test_logout(request):
    logout(request)
    return redirect('home')

    # return render (request ,'seniorapp\\home_test.html', {'user':request.user})


# def test_login(request):
#     if request.method == 'POST':
#         pass
#     else:
#         form = StudentLoginForm()
#         pass
#     # student = Student.objects.get(student_id = '20152340')
#     username = '20152340'
#     password = 'qwaszxerdfcv'
#     user = authenticate(request, username=username, password=password)
#     login(request, user)
#     # if user is not None:
#     #     # Redirect to a success page.
#     #     logged_in = True
#     #     ...
#     # else:
#     #     # Return an 'invalid login' error message.
#     #     ...
#     #         # student.login
#     # user = getattr(request, 'user', None)
#     # if not getattr(user, 'is_authenticated', True):
#     #     user = None
#     # # user_logged_out.send(sender=user.__class__, request=request, user=user)
#     # request.session.flush()
#     # if hasattr(request, 'user'):
#     #     from django.contrib.auth.models import AnonymousUser
#     #     request.user = AnonymousUser()
#     # user.is_authenticated
#     # logout(request)
#     # user.objects.model
#     # user._meta.db_table
#     # user.__class__.objects.model
#     table_name = user._meta.db_table # this will work too
#     return render (request ,'seniorapp\\test_login.html', {'user':request.user})
#     # return render (request ,'seniorapp\\test_login.html', {'user':user})

# def test_home(request):
#     # student = Student.objects.get(student_id = '20152340')
#     username = '20152340'
#     password = 'qwaszxerdfcv'
#     user = authenticate(request, username=username, password=password)
#     login(request, user)

#     # if user is not None:
#     #     # Redirect to a success page.
#     #     logged_in = True
#     #     ...
#     # else:
#     #     # Return an 'invalid login' error message.
#     #     ...
#     #         # student.login
#     # user = getattr(request, 'user', None)
#     # if not getattr(user, 'is_authenticated', True):
#     #     user = None
#     # # user_logged_out.send(sender=user.__class__, request=request, user=user)
#     # request.session.flush()
#     # if hasattr(request, 'user'):
#     #     from django.contrib.auth.models import AnonymousUser
#     #     request.user = AnonymousUser()
#     # user.is_authenticated
#     logout(request)
#     return render (request ,'seniorapp\\test_home.html', {'user':request.user})
