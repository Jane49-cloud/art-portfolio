from django.contrib import admin
from .models import Testimonial, Picture


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class PictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Picture)
admin.site.register(Testimonial)
