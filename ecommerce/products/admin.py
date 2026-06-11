from django.contrib import admin
from user.models import User
from .models import Product

admin.site.register(User)
admin.site.register(Product)



