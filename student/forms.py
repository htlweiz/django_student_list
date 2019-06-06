"""
Forms used to modify your objects should be defined here.
"""

from django import forms

class StudentForm(forms.Form):
    """ A form to modify a single Student object """
    first_name = forms.CharField(label="First Name", max_length=200)
    sure_name = forms.CharField(label="Sure Name", max_length=200)
    birth_date = forms.DateField(label=" Birth Date")
