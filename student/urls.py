"""
in this file all urls for the students app are defined.
this file is included by ../studentList/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='student_list'),
        path('<int:student_id>', views.detail, name='student_detail'),
        path('create', views.create, name='student_create'),
        path('<int:student_id>/delete', views.delete, name='student_delete'),
        ]
