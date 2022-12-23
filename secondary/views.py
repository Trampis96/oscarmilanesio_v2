from django.shortcuts import render
from .models import Image
from django.views.generic import ListView 
# Create your views here.

def HomeView(request):
    return render(request,'index.html',{})

class GalleryView(ListView):
    model=Image
    fields='__all__'
    template_name='gallery.html'

def AboutUsView(request):
    return render(request,'about_us.html',{})