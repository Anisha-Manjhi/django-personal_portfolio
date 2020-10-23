from django.db import models

class Blog(models.Model):
    blogname = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    date= models.DateField()