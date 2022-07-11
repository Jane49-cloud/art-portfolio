from django.shortcuts import render
from django.http import HttpResponse
from .models import Testimonial, Picture


def index(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'index.html',
                  {"testimonials": testimonials})


def about(request):
    return render(request, 'About.html')


def contact(request):
    return render(request, 'contact.html')


def work(request):
    pictures = Picture.objects.all()
    return render(request, 'work.html',
                    {"pictures": pictures})
