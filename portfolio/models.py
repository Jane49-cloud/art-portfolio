from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=40)
    message = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=5000)


class Picture(models.Model):
    name = models.CharField(max_length=40)
    Description = models.CharField(max_length=5000)
    image_url = models.CharField(max_length=5000)

