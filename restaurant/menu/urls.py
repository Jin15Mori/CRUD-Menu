from django.contrib import admin
from django.urls import path,include
from menu import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.show, name = "show"),
    path("delete/<int:id>", views.delete, name = "delete"),
    path("update/<int:id>", views.update, name = "update"),
    path("update/updaterecord/<int:id>", views.updaterecord, name = "updaterecord")
]
