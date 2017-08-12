from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from onlinetut.forms import UserForm
from .models import Courses,Tutorials


def index(request):
    return  render(request,'index.html',)

@login_required
def DetailView(request,pk):
    obj = Tutorials.objects.filter(albums_id=pk).order_by('id')
    return render(request,'detail.html',{'course':obj})

@login_required
def VideoView(request,pk):
    obj = Tutorials.objects.filter(albums_id=pk)
    return render(request,'video.html',{'course':obj})

@login_required
def HomepageView(request):

    return render(request,'course_list.html',{'list':Courses.objects.all()})


def registerUser(request):
    if request.method =="POST":
        userform= UserForm(request.POST)

        if userform.is_valid():
            newuser=userform.save(commit=False)
            newuser.set_password(userform.cleaned_data['password'])
            newuser.save()
            return render(request,'registration_completed.html',{'user':newuser})

    else:
        userform=UserForm()


    return render(request,'registration.html',{'userform':userform})
# def user_login(request):
#         if (request.method == "POST"):
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             if (username == "ruku" and password == "17NaimaRUKU17"):
#                 user = authenticate(username=username, password=password)
#             else:
#                 user = authenticate(username=username, password=password)
#
#             if (user):
#                 if (user.is_active):
#                     login(request, user)
#                     # return HttpResponseRedirect(reverse('index.html'))
#                     return render(request, 'web/course_list.html')
#                 else:
#                     return HttpResponse("Account Not Active")
#             else:
#                 print("Someone Tried to login and Failed")
#                 return HttpResponse("Invalid Login")
#
#         else:
#             return render(request, 'web/login.html', {})
#
# @login_required
# def user_logout(request):
#         logout(request)
#         # return HttpResponseRedirect(reverse('basic_app/index.html'))
#         return render(request, 'web/index.html')
