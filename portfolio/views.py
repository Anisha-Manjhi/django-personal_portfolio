from django.shortcuts import render
from .models import Project

def home(request):
    projects=Project.objects.all()
    return render(request , 'portfolio/home.html',{'projects':projects})
def technical(request):

    return render(request,'portfolio/technical.html')


def softskill(request):
    return render(request, 'portfolio/softskill.html')
