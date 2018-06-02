from django.urls import path
from . import views

#set up you app urls here

urlpatterns = [
    path('', views.index),  #the path for our index view
]