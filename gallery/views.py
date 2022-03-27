from tkinter import Image
from django.shortcuts import render,redirect
from django.http import Http404
from .models import Photo, Location, Category

# Create your views here.
def welcome(request):
    images = Photo.objects.all()
    locations = Location.all_locations()
    return render(request,'welcome.html', {'images':images, 'locations':locations})


