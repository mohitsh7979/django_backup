
from django.contrib import admin
from django.urls import path
from authenticationapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Customer/',views.Customer_details,name="Customer"),
    path('Register/',views.register),
    path('login/',views.loginhandle),
    path('profile/',views.profile_page),
    path('logout/',views.logouthandle)

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
