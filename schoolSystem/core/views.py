from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SchoolClass, Teacher, Parent, Student, Message

# Create your views here.

@login_required
def my_view(request):
    if request.user.roles == "teacher":
        teacherData = Teacher.objects.get(user = request.user)
        messages = Message.objects.filter(SchoolClass = teacherData.teacherClass)
        return render(
        request,
        "core/teacher.html",
        {
            "school_class": teacherData.teacherClass,
            "messages": messages
        }
        )
    return redirect("/")


