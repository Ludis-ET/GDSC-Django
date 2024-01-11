from django.db import models

# Create your models here.
class Comment(models.Model):
    #content, created time, and modified time.
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name