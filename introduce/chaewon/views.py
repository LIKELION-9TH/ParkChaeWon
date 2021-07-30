from django.shortcuts import redirect, render
from .models import Porfolio

# Create your views here.


def home(request):
    return render(request,'home.html')

def hobby(request):
    return render(request,'hobby.html')
    
def music(request):
    porfolios=Porfolio.objects
    return render(request,'music.html',{'porfolios':porfolios})
    
def photo(request):
    return render(request,'photo.html')
    
def place(request):
    return render(request,'place.html')

def create(request):
    portfolio=Porfolio()
    portfolio.title=request.GET['title']
    portfolio.description=request.GET['description']
    portfolio.save()
    return redirect('/music/')

def edit(request,id):
    edit_music=Porfolio.objects.get(id=id)
    return render(request,'edit.html',{'edit_music':edit_music})



def delete(request,id):
    delete_music=Porfolio.objects.get(id=id)
    delete_music.delete()
    return redirect('music')

def update(request,id):
    update_music=Porfolio.objects.get(id=id)
    update_music.title=request.POST['title']
    update_music.description=request.POST['description']
    update_music.save()
    return redirect('/music/')