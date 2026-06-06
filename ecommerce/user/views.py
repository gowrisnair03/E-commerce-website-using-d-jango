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
        phone_number=request.POST.get("phone_number")

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            phone_number=phone_number,
          
        )
        return redirect('index')

    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

    
def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            return render(request, "index.html")

    return render(request, "login.html")

def error404(request):
    return render(request ,"404.html")

def testimonial(request):
    return render(request,"testimonial.html")    


def chackout(request):
    return render(request ,"chackout.html")    

def cart(request):
    return render(request, "cart.html")    


def shopdetail(request):
    return render(request, "shop-detail.html")

def shop(request):
    return render(request,"shop.html")

    
def logout_view(request):
    return HttpResponse("Logout Page")