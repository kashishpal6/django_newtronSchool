from django.contrib import admin
from django.urls import path
from emp_app import views


urlpatterns = [
    path("",views.index,name='emp_app')
    
]
