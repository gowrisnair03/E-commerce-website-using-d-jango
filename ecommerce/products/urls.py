from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_product, name='create'),
    path('update/<int:id>/', views.update_product, name='update'),
    path('delete/<int:id>/', views.delete_product, name='delete'),
    path('shop/', views.shop, name='shop')
    
]