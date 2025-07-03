from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
   context = {}
   return render(request,'main.html',context)

def about(request):
    return render(request,'home.html')

