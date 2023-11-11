from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Quiz)
# admin.site.register(Question)
# admin.site.register(Choice)
# admin.site.register(Answer)
# admin.site.register(UserResponse)

@admin.register(Quiz)
class AdminQuiz(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(Question)
class AdminQuestions(admin.ModelAdmin):
    list_display = ['id','quiz','text']

@admin.register(Choice)
class AdminChoice(admin.ModelAdmin):
    list_display = ['id','question','text']

@admin.register(Answer)
class AdminAnswer(admin.ModelAdmin):
    list_display = ['id','question','choice']

@admin.register(UserResponse)
class AdminUserResponse(admin.ModelAdmin):
    list_display = ['id','user','question','selected_choice']