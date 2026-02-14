from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Teacher, Parent, Student, Message

# Create your views here.

@login_required
def my_view(request):
    if request.user.role == "teacher":
        teacherData = Teacher.objects.get(request.user)
        messages = Message.objects.filter() # Указать параметры для фильтрации
        



