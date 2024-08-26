from django.shortcuts import render
from django.http import  HttpResponse
import datetime
# Create your views here.


def home(request):
    isActive=True
    if request.method == 'POST':
             check=request.POST.get('check')
             print(check)
             if check is None: isActive=False
             else:isActive=True

    date=datetime.datetime.now()
    
    name="Code with Dani"
    List_of_program=[
        "WAP to check even or odd",
        "WAP to check prime number"
    ]
    student_data={
        'student_name':'ali',
        'student_collage':'alpha',
        'student_city':'punjab'
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_program':List_of_program,
        'student_data':student_data
    }

    return render(request, 'home.html',data)


def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')
