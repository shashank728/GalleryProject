from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('Gallery/',views.gallery,name="gallery"),
    path('add_img/',views.add_img,name="add_img"),
    path('delete_img/<int:imgs_id>',views.delete,name="delete"),
    path('category/',views.category,name="category"),

        

    
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
