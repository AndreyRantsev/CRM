from urllib import request

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SchoolClass, Teacher, Parent, Student, Message, FAQ
from django.db.models import Q

# Create your views here.

@login_required
def my_view(request) -> HttpResponse | HttpResponseRedirect:

    if request.user.roles == "teacher":
        teacherData = Teacher.objects.get(user = request.user)
        messages = Message.objects.filter(Q(SchoolClass = teacherData.teacherClass)|Q(SchoolClass__isnull=True))

        faq = FAQ.objects.all()

        return render(
        request,
        "core/teacher.html",
        {
            "name": teacherData.user.username,
            "school_class": teacherData.teacherClass,
            "messages": messages,
            "faqs": faq
        }
        )
    
    
    if request.user.roles == "student":
        studentData = Student.objects.get(user = request.user)
        messages = Message.objects.filter(Q(SchoolClass = studentData.studentClass)|Q(SchoolClass__isnull=True))
        return render(
            request,
            "core/student.html",
            {   
                "name": studentData.user.username,
                "school_class": studentData.studentClass,
                "messages": messages
            }
            )
    if request.user.roles == "parent":
        parentData = Parent.objects.get(user = request.user)
        children = parentData.children.all()
        messages = Message.objects.filter(Q(SchoolClass__student__in=children) | Q(SchoolClass__isnull=True))
        return render(
            request,
            "core/parent.html",
            {   
                "name": parentData.user.username,
                "children": children,
                "messages": messages
            }
            )

    return redirect("/")

