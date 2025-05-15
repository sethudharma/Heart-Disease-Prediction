# myapp/urls.py
from django.urls import path
from django.urls import re_path as url # Import the url function
from .views import index,result,HomePage,SignupPage,LoginPage,LogoutPage


urlpatterns = [
    path('',HomePage,name='home'),
    path('index/', index, name='index'),
    # path('result/', result, name='result'),
    path('index/result/', result, name='result'),
    path('signup/',SignupPage,name='signup'),
    path('login/',LoginPage,name='login'),
    path('logout/',LogoutPage,name='logout'),
]