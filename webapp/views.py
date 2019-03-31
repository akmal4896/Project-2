from django.shortcuts import render
from django.http import HttpResponse

def webhome(request):
    return render(request, 'webapp/home.html')
