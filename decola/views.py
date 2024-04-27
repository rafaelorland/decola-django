from django.http import HttpResponse
from django.shortcuts import render



def helloworld(request):
    return HttpResponse("<h1>Hello World</h1>")

def home(request):
    return render(request, 'home/pages/home.html')

def not_found_404(request, exception):
    return render(request, 'error/404.html', status=404)