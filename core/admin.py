from django.contrib import admin
from .models import (User, Teacher, Parent, Student, SchoolClass, FAQ, Message)
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'roles')
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Роль', {'fields': ('roles',)}),
    )

admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(SchoolClass)
admin.site.register(FAQ)
admin.site.register(Message)
