from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Helloo")

def about(request):
    return HttpResponse("About")
