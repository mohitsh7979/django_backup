from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
 
    path('',views.loginhandle),
    path('forget-password/',views.ForgetPassword),
    path('logout/',views.logouthandle),
    path('change-password/<token>/',views.ChangePassword , name='change_password'),
]

