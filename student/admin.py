"""
By registering your models in admin.site the model can be reached and managed by accessing /admin in your webapplication
"""
from django.contrib import admin

from .models import Student

# Register your models here.

admin.site.register(Student)

