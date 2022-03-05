from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Myself/home.html')
def Animals(request):
    return render(request, 'Myself/Animals.html')

def Plants(request):
    return render(request, 'Myself/Plants.html')

def Clothes(request):
    return render(request, 'Myself/Clothes.html')

def People(request):
    return render(request, 'Myself/People.html')


