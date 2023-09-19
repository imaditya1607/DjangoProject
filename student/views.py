from django.http import HttpResponse
from django.shortcuts import render
from .models import Student


def homepage(request):
    return render(request, 'Homepage.html')


def add_student(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        pass
    else:
        return HttpResponse("Sorry .. Please Try again")


    return render(request, 'Add_Student.html')


def all_student(request):
    student = Student.objects.all()
    context = {
        'student': student
    }
    return render(request, 'All_Student.html',context)


def remove_student(request):
    return render(request, 'Remove_Student.html')
