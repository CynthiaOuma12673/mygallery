from django.conf.urls import url
from . import views
urlpatterns = [
        url('',views.welcome,name='galleryHome'),
        url('search/', views.get_category,name ='category'),
        url('location/<str:search_location>/',views.get_location,name='location'),
        url('image/<int:image_id>/',views.get_image,name='image'),
]