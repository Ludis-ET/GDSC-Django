from django.db import models

# Create your models here.
class Comment(models.Model):
    #content, created time, and modified time.
    name = models.CharField