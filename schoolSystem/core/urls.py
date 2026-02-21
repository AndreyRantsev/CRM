from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path("", views.my_view, name = "my_view"),
    path("login/", auth_views.LoginView.as_view(template_name = "core/login.html"), name = "login"),
]
