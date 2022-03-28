from email import message
from re import search
from tkinter import Image
from turtle import title
from django.shortcuts import render,redirect
from django.http import Http404
from .models import Photo, Location, Category

# Create your views here.
def welcome(request):
    images = Photo.objects.all()
    locations = Location.all_locations()
    return render(request,'welcome.html', {'images':images, 'locations':locations})

def get_category(request):
    title = 'Category'
    locations = Location.objects.all()

    if 'category' in request.GET and request.GET['category']:
        search_category = request.GET.get('category')
        searched_category = Photo.search_image(search_category)
        message = f"{search_category}"

        return render(request, 'all-gall/search.html', {'message':message,'images':searched_category,'title':title,'locations':locations})
    else:
        message = "You need search a category kindly search"
        return render(request, 'all-gall/search.html',{'message':message})

def get_location(request, search_location):
    title = 'Location'
    locations = Location.objects.all()
    images = Photo.filter_by_location(search_location)
    message = f"{search_location}"
    return render( request, 'all-gall/location.html',{'images':images, 'locations':locations,'title':title, 'message':message})

def get_image(request, image_id):
    try:
        image = Photo.objects.get(id = image_id)
    except:
        raise Http404()
    return render(request, 'all-gall/image.html',{'image':image})
