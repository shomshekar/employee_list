from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    empid = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, null=True)
    empstatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"