from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.forms.models import model_to_dict

from . import forms
from .models import Employee

# Create your views here.
def updateEmployee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = forms.FormName(request.POST)
        # Then we check to see if the form is valid
        if form.is_valid():
            employee.firstname=form.cleaned_data['firstname']
            employee.lastname=form.cleaned_data['lastname']
            employee.email=form.cleaned_data['email']
            employee.save() 
            # Redirecting to another url
            return redirect("/employee-list/")
    else:    
        # prepopulate the form with an existing Employee
        form = forms.FormName(initial=model_to_dict(employee))
        return render(request, "updateEmployee.html", {'form':form})

def deleteEmployee(request, id):
    # employee = get_object_or_404(Employee, pk=id)  # Get your current employee
    employee = Employee.objects.get(id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect("/employee-list/")


def addEmployee(request):
    # template = loader.get_template('addEmployee.html')
    # return HttpResponse(template.render())
    form = forms.FormName()
    # Check to see if we are getting a POST request back
    if request.method == "POST":
        form = forms.FormName(request.POST)
        # Then we check to see if the form is valid
        if form.is_valid():
            employee = Employee(firstname=form.cleaned_data['firstname'], lastname=form.cleaned_data['lastname'], email=form.cleaned_data['email'])
            employee.save() 
            # Calling another fuction within another function
            # return employees(request)
            # Redirecting to another url
            return redirect("/employee-list/")

    return render(request, "addEmployee.html", {'form':form})

def employees(request):
    employees = Employee.objects.all().values()
    template = loader.get_template('all_employee.html')
    context = {
    'employees': employees,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    employee = Employee.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'employee': employee,
    }
    return HttpResponse(template.render(context, request))