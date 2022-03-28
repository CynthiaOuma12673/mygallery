import re
from django.shortcuts import render,redirect
from django.http import Http404
from .models import Photo, Location, Category

# Create your views here.
def welcome(request):
    images = Photo.objects.all()
    locations = Location.objects.all()
    return render(request,'welcome.html', {'images':images, 'locations':locations})

def get_category(request):

    if 'category' in request.GET and request.GET['category']:
        search_category = request.GET.get('category')
        searched_category = Photo.search_image(search_category)
        message = f"{search_category}"

        return render(request, 'all-gall/search.html', {'message':message,'images':searched_category})
    else:
        message = "You need search a category kindly search"
        return render(request, 'all-gall/search.html',{'message':message})

def get_location(request, search_location):
    if 'location' in request.GET and request.GET['location']:
        filters = request.GET.get('location')
        found = Photo.filter_loca(filters)
        message = f'{filters}'
        locations = Location.objects.all()
    return render( request, 'all-gall/location.html',{"message":message,"found":found,"locations":locations})

def get_image(request,id):
    try:
        image = Photo.objects.get(id = id)
    except:
        raise Http404()
    return render(request, 'all-gall/image.html',{'image':image})

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        search_category = Category.search_image(search_term)
        message = f"{search_category}"

        return render(request, 'all-gall/search.html', {'message':message,'images':search_category})
    else:
        message = "You need search a category kindly search"
        return render(request, 'all-gall/search.html',{'message':message})


