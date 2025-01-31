from django.contrib import admin
from django.urls import path

# Register your models here.
from .models import FAQ

admin.site.register(FAQ)