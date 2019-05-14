""" models for the student app are defined in this file """
from django.db import models

# Create your models here.

class Student(models.Model):
    """ A simple class holding all informations for a single student """
    first_name = models.CharField(max_length=200)
    sure_name = models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        """ defines the pretty print of this class used eg. in admin area """
        return "%s %s : %s" % (self.first_name, self.sure_name, self.birth_date)
