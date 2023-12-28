from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "empstatus")

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)