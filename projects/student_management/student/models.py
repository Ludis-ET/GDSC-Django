from django.db import models
from advisor.models import Advisor

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    student_id = models.CharField(max_length=255)
    advisor = models.ForeignKey(Advisor,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.name
