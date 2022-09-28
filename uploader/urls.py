
# from django.contrib import admin
from django.urls import path
from uploader import views 


# app_name = "uploader" 

urlpatterns = [
    path('', views.index, name="home"),
    
]


# from django.urls import path  
# from .views import image_request  
  
# app_name = 'uploader'  
# urlpatterns = [  
#     path('', image_request, name = "uploader")  
# ]
