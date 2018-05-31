from __future__ import unicode_literals
from django.db import models
from PIL import Image
from time import time

def upload_blog_image(instance, filename):
    return "blog_content_image/%s_%s" % (str(time()).replace(".", "_"), filename)

def profile_image(instance, filename):
    return "profile_image/%s_%s" % (str(time()).replace(".", "_"), filename)

# Create your models here.
class Blogger(models.Model):
    UNIVERSITIES = (
        ("JKUAT", 'Jommo Kenyatta University of Agriculture and technology'),
        ('UON', 'University of Nairobi'),
        ('KU', 'Kenyatta University'),
        ("STRATH", "Strathmore"),
        ("DAYSTAR", "Daystat University"),
        ("CUEA", "Cooperative University of East Africa"),
    )
    PLACE = (
        ("Juja", "Juja"),
        ("Nairobi","Nairobi"),
        ("Kahawa","Kahawa"),
        ("Madaraka","Madaraka"),
        ("Athi-River","Athi-River"),
        ("Karen","Karen")
    )
    name = models.CharField(max_length=120, null=False)
    info = models.TextField("Profile bio", blank=True, null=True)
    profile_image = models.FileField(upload_to=profile_image, null=False, blank=True)
    place_from = models.TextField("Place from", choices=PLACE, max_length=1, null=False, blank=True)
    university_name = models.TextField("University from", max_length=1, choices=UNIVERSITIES, null=True, blank=True)
    course_name = models.CharField("Course undertaking",max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    Category = (
        ("Travelling","Travelling"),
        ("Work","Work"),
        ("Lifestyle","Lifestyle"),
        ("Photography","Photography"),
        ("Finance","Finance"),
        ("Programming","Programming"),
        ("Food & Drinks","Food & Drinks"),
        ("Technology","Technology"),
        ("Engineering","Engineering"),
        ("Science","Science"),
        ("Law","Law"),
        ("Health","Health"),
        ("Agriculture","Agriculture"),
        ("Enterprenuership","Enterprenuership"),
        ("Cars", "Cars"),
    )
    title = models.CharField(max_length=120, null=False)
    blog_text = models.TextField(blank=False, null=False)
    blog_image = models.FileField(upload_to=upload_blog_image, null=True, blank=True)
    category = models.TextField(choices=Category, max_length=5, null=True, blank=False)
    publish_date = models.DateTimeField("Date published", null=True)
    likes = models.IntegerField(default=0)
    blogger = models.ForeignKey(Blogger, on_delete=models.DO_NOTHING , null=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(blank=False)
    publish_date = models.DateTimeField("Date published")
    blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING,null=False)
