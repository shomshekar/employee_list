from django.urls import path
from . import views

urlpatterns = [
    path('employee-list/', views.employees, name='employee-list'),
    path('employee-list/details/<int:id>', views.details, name='view-employee'),
    path('add-employee/', views.addEmployee, name='add-employee'),
    path('employee-list/update/<int:id>', views.updateEmployee, name='update-employee'),
    path('employee-list/delete/<int:id>', views.deleteEmployee, name='delete-employee'),
]
