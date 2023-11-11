from django.contrib import admin
from django.urls import path
from auth_app import views

urlpatterns = [

    path('',views.login_handle),
    path('create-account/',views.Create_Account),
    path('logout/',views.logouthandle)
]
