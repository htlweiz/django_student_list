from django.db import models
from student.models import Student

# Create your models here.

class Course(models.Model):
    """ A simple class holding all informations for a single course """
    course_name = models.CharField(max_length=200)
    ects = models.FloatField()

    students = models.ManyToManyField(Student)
    pass

