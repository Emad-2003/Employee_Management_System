from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addEmp',views.addEmp,name="addEmp"),
    path('allEmp',views.allEmp,name="allEmp"),
    path('flrEmp',views.flrEmp,name="flrEmp"),
    path('remEmp',views.remEmp,name="remEmp"),
    path('remEmp/<int:emp_id>',views.remEmp,name="remEmp")
    

]