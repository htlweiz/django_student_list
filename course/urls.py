"""
in this file all urls for courses app are defined.
this file is included by ../studentList/urls.py
"""

from django.urls import path
from . import views

urlpatterns = [
        path('<int:course_id>', views.detail, name='course_detail'),
        ]

