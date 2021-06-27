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


def Home(request):
    return render(request, 'frontend/index.html')

def ABOUT(request):
    return render(request, 'frontend/about.html')

def CONTACT(request):
    return render(request, 'frontend/contact.html')

def GALLERY(request):
    return render(request, 'frontend/gallery.html')

def PRICING(request):
    return render(request, 'frontend/pricing.html')

