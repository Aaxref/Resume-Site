from django import forms
from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    response = models.TextField(blank=True, null=True)  # اضافه کردن فیلد response

    def __str__(self):
        return self.name

