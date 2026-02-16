from django.shortcuts import render

def home(request):
    return render(request, 'myapp/index.html')

def get_started(request):
    return render(request, 'myapp/get_started.html')