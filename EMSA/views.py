from datetime import datetime
from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def allEmp(request):
    emps = Employee.objects.all()
    context={
        'emps' : emps
    }
    print(context)
    return render(request,'allEmp.html',context)

def addEmp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        
        #adding he user
        new_emp=Employee(first_name=first_name,
                         last_name=last_name,
                         salary=salary,
                         bonus=bonus,
                         phone=phone,
                         dept_id=dept,
                         role_id=role,
                         hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')
        
    elif request.method=='GET':
        return render(request,'addEmp.html')
    else:
        return HttpResponse('An Exception has Occurred !! Employee has not been Added ')
       

def flrEmp(request):
    if request.method == 'POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        
        emps=Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        
        context = {'emps':emps}
        return render(request,'allEmp.html',context)
   
    elif request.method == 'GET':
        return render(request,'flrEmp.html')
    
    else:
        return HttpResponse("An error occurred")
       

def remEmp(request,emp_id=0):
    if emp_id:
        try:
            emp_rid=Employee.objects.get(id=emp_id)
            emp_rid.delete()
            return HttpResponse('Employee Removed successfully')
        except:
            return HttpResponse('Please Enter a valid EMP id')
    
    emps= Employee.objects.all()
    context={'emps':emps}
    return render(request,'remEmp.html',context)