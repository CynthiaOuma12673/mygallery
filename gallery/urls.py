from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url('',views.welcome,name='galleryHome'),
        url('search/', views.get_category,name ='category'),
        url('location/<str:search_location>/',views.get_location,name='location'),
        url('image/<int:image_id>/',views.get_image,name='get_image'),
]
if settings.DEBUG:
        urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
        urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)