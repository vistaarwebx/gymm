
from django.contrib import admin
from django.urls import path
from zmain.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include


urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('',Home,name= 'home'),
    path('about',ABOUT,name= 'about'),
    path('contact',CONTACT,name= 'contact'),
    path('gallery',GALLERY,name= 'gallery'),
    path('product',PRODUCT,name= 'product'),
    path('services',SERVICES,name= 'services'),
    path('blog',BLOG,name= 'blog'),

    #########dynamic urls ######
    path('blog_single/<int:blo_id>/',BLOG_SINGLE, name='blog_single'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
