from django.shortcuts import render, HttpResponse
from .models import Employee,Roles,Department
from datetime import datetime
from django.db.models import Q
def home_view(request):
    return render(request, 'employee/index.html')

def view_emp(request):
    emps = Employee.objects.all()
    print(f"Total employees: {emps.count()}")  # Check how many records exist
    print(f"Employees: {emps}")
    for emp in emps:
        print(f"  - {emp.first_name} {emp.last_name}")
    context = {
        'emps': emps
    }
    return render(request, 'employee/view_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department_id = request.POST['dept']
        role_id = request.POST['role']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone_number = int(request.POST['phone_number'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, dept_id=department_id, role_id=role_id, hire_date=datetime.now(), phone=phone_number)
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    
    departments = Department.objects.all()
    roles = Roles.objects.all()
    context = {
        'departments': departments,
        'roles': roles
    }
    return render(request,'employee/add_emp.html', context)
    

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
            
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'employee/remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept=dept)
        if role:
            emps = emps.filter(role=role)

        context = {
            'emps': emps
        }
        return render(request, 'employee/view_emp.html', context)

    elif request.method == 'GET':
        departments = Department.objects.all()
        roles = Roles.objects.all()
        context = {
            'departments': departments,
            'roles': roles
        }
        return render(request, 'employee/filter_emp.html', context)
    else:
        return HttpResponse('An Exception Occurred')