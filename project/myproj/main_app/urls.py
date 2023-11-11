from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from main_app import views

urlpatterns = [

    path('table/',views.project_table_data,name="table"),
  
]
