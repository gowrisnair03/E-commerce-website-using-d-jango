from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product

# List all products
def home(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

# Create Product
def create_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            price=request.POST.get("price")
        )
        return redirect("home")

    return render(request, "create_product.html")

# Update Product
def update_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.save()
        return redirect("home")

    return render(request, "update_product.html", {"product": product})

# Delete Product
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product.delete()
        return redirect("home")

    return render(request, "delete_product.html", {"product": product})


def shop(request):
    products = Product.objects.all()
    for product in products:
        print(product.name)
    return render(request,"shop.html",{"products":products})