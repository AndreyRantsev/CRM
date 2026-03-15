from urllib import request

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SchoolClass, Teacher, Parent, Student, Message, FAQ, User
from django.db.models import Q

# Create your views here.

@login_required
def my_view(request) -> HttpResponse | HttpResponseRedirect:

    if request.user.roles == "teacher":
        teacherData = Teacher.objects.get(user = request.user)

        if request.method == "POST":
            title = request.POST.get("title")
            text = request.POST.get("text")
            Message.objects.create(
                author = request.user,
                title = title,
                text = text,
                SchoolClass = teacherData.teacherClass
            )
            return redirect("my_view")
        
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
        faq = FAQ.objects.all()

        return render(
            request,
            "core/student.html",
            {   
                "name": studentData.user.username,
                "school_class": studentData.studentClass,
                "messages": messages,
                "faqs": faq
            }
            )
    if request.user.roles == "parent":
        parentData = Parent.objects.get(user = request.user)
        children = parentData.children.all()
        messages = Message.objects.filter(Q(SchoolClass__student__in=children) | Q(SchoolClass__isnull=True))
        faq = FAQ.objects.all()
        return render(
            request,
            "core/parent.html",
            {   
                "name": parentData.user.username,
                "children": children,
                "messages": messages,
                "faqs": faq
            }
            )
    
    if request.user.roles == "admin":
        messages = Message.objects.all()

        if request.method == "POST" and "message" in request.POST:
            title = request.POST.get("title")
            text = request.POST.get("text")
            class_id = request.POST.get("school_class")
            school_class = None

            if class_id:
                school_class = SchoolClass.objects.get(id = class_id)

            Message.objects.create(
                author = request.user,
                title = title,
                text = text,
                SchoolClass = school_class
            )
            return redirect("my_view")
        
        if request.method == "POST" and "faq" in request.POST:
            question = request.POST.get("question")
            answer = request.POST.get("answer")

            FAQ.objects.create(
                question = question,
                answer = answer
            )
        
        faq = FAQ.objects.all()
        classes = SchoolClass.objects.all()
        return render(
            request,
            "core/admin-template.html",
            {   
                "messages": messages,
                "faqs": faq,
                "classes": classes
            }
        )
    return redirect("login")

    
