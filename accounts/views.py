from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
@csrf_exempt
def testMe(request):
    pickup_records = []
    pickup_records.append({
            "id": 1,
            "name": "Naveen"
    });
    pickup_records.append({
            "id": 2,
            "name": "Gaurav"
    });
    return JsonResponse(pickup_records, safe=False)
def register(request):

    name = request.POST['First_name']
    lname = request.POST['Last_name']
    uname = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    mail = request.POST['email']

    if User.objects.filter(username=uname).exists():
        return HttpResponse("User already available")
    else:
        user=User.objects.create_user(username=uname,password=password1,email=mail,first_name=name,last_name=lname)
        user.save()
        print("user created")
        return HttpResponse("You are logged in successfully")
def reg_view(request):
    return render(request,'register.html')
def login_view(request):
    return render(request,'login.html')
def logeed_in(request):
    usern = request.POST['username']
    pwd = request.POST['password1']
    uobj= auth.authenticate(request,username=usern,password=pwd)
    if uobj:
        return HttpResponse("Logged in...")
    else:
        return HttpResponse("Invalid creadentials...")

