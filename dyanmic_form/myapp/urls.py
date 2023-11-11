# from django.urls import path
# from . import views

# urlpatterns = [
#     # URL for displaying the resume form
#     path('create_resume/', views.create_resume, name='create_resume'),

#     # URL for the success page (customize the path as needed)

# ]


from django.urls import path
from . import views

urlpatterns = [
    path('resume-form/', views.resume_form, name='resume_form'),
    path('success/', views.success, name='success'),
]

