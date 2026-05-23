from django.shortcuts import render
from .models import User
# Create your views here.
def register(request):

    return render(request, 'user/register.html')

def login_view(request):

    return render(request, 'user/login.html')

def logout_view(request):

    return render(request, 'user/logout.html')