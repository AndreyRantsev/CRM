from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "админ"),
        ("teacher", "учитель"),
        ("parent", "родитель"),
        ("student", "ученик")
    )

    roles = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

class SchoolClass(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return self.name
    
class Teacher(models.Model):
    user =  models.OneToOneField("User", on_delete = models.CASCADE)
    teacherClass = models.OneToOneField("SchoolClass", on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} {self.teacherClass.name}"

class Student(models.Model):
    user =  models.OneToOneField("User", on_delete=models.CASCADE)
    studentClass = models.ForeignKey ("SchoolClass", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.user.username} {self.studentClass.name}"

class Parent(models.Model):
    user =  models.OneToOneField("User", on_delete=models.CASCADE)
    children = models.ManyToManyField("Student")
    def __str__(self) -> str:
        return f"{self.user.username}"

class Message(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField()
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    SchoolClass = models.ForeignKey("SchoolClass", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Выберите класс. Если оставить пустым - отправится всем")

    def __str__(self) -> str:
        return f"{self.author} {self.title} {self.text} {self.time} {self.SchoolClass}"
    
class FAQ(models.Model):
    question = models.CharField()
    answer = models.TextField()

    def __str__(self) -> str:
        return f"{self.question} {self.answer}"