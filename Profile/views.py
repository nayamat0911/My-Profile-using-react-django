from django.shortcuts import render

# Create your views here.

def homepage(request):
    diction = {}
    return render(request, 'Profile/index.html', context=diction)

def home(request):
    diction = {}
    return render(request, 'index.html', context=diction)

def profile(request):
    diction = {}
    return render(request, 'profile.html', context=diction)