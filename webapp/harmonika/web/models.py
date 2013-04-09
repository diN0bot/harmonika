from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    gap = models.IntegerField()
    description = models.TextField()

class Organization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
