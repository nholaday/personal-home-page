from django.shortcuts import render

def index(request):
    return render(request, 'homepage_app/index.html')
