from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zmain.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from gymm.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User

URL = "http://18.205.215.155:8000/contactapi/"
def Home(request):
    return render(request, 'frontend/index.html')

def ABOUT(request):
    return render(request, 'frontend/about.html')

def CONTACT(request):
    if request.method == "POST":
        f = request.POST
        content = f['message']
        nam = f['name']
        ema = f['email']
        subject = f['subject']
        email = 'tejendrapatel1998@gmail.com'
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
        d = {'subject': subject, "content": content}
        html = get_template('email/email.html').render(d)
        msg.attach_alternative(html, 'text/html')
        msg.send()
        contactss.objects.create(name=nam,subject=subject,Email=ema,message=content)

    return render(request, 'frontend/contact.html')

def GALLERY(request):
    gal = Gallery.objects.all()
    d = {"gal":gal}
    return render(request, 'frontend/gallery.html',d)

def PRODUCT(request):
    pro = Product.objects.all()
    d = {"pro":pro}
    return render(request, 'frontend/product.html',d)

def SERVICES(request):
    ser = Services.objects.all()
    d = {"ser":ser}
    return render(request, 'frontend/services.html',d)

def BLOG(request):
    blo = Blog.objects.all()
    d = {"blo":blo}
    return render(request, 'frontend/blog.html',d)

########dynamic pages ######
def BLOG_SINGLE(request,blo_id):
    blosingle = Blog.objects.get(id=blo_id)
    d = {"blosingle":blosingle}
    return render(request, 'frontend/blog_details.html',d)

