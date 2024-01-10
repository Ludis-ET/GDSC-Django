from django.db import models

# Create your models here.
class Advisor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    def __str__(self):
        return self.name
