from django.http import HttpResponse
from django.shortcuts import render
from harmonika.web.models import Student, Organization

def organization(request):
    org = Organization.objects.all()[0]
    return render(request, 'web/organization.html', {'org': org})

def students(request):
    students = Student.objects.order_by('?')
    return render(request, 'web/students.html', {'students': students})

def student(request, slug):
    student = Student.objects.get(slug=slug)
    return render(request, 'web/student.html', {'student': student})
