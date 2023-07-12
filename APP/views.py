from django.shortcuts import render

#import loader
from django.template import loader

# Create your views here.
def stop_watch(request):
    return render(request,'index.html')
