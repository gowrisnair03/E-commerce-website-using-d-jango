from .import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('404/', views.error404, name='404'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('chackout/',views.chackout, name='chackout'),
    path('cart/',views.cart, name='cart'),
    path('shop-detail/',views.shopdetail, name='shop-detail'),
    path('shop/',views.shop ,name='shop'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
]