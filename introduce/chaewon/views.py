from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def hobby(request):
    return render(request,'hobby.html')