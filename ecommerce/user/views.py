from django.shortcuts import render
from .models import User
from django.shortcuts import render
from django.http import HttpResponse


def register(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
          
        )
        print(User)

    return render(request, 'register.html')

def login_view(request):
    return HttpResponse("Login Page")


def logout_view(request):
    return HttpResponse("Logout Page")