from django.contrib import admin
from .models import *

@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number']