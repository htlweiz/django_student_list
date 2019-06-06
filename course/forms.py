"""
Forms used to modify your objects should be defined here.
"""

from django import forms
from student.models import Student

class CourseForm(forms.Form):
    """ A form to modify a single Student object """
    course_name = forms.CharField(label="Name", max_length=200)
    ects = forms.FloatField()
    st = forms.ModelMultipleChoiceField(label="Students",
                                        required=False,
                                        queryset=Student.objects.order_by('sure_name', 'first_name'),
                                        )

    def __init__(self, *args, **kwargs):
        """ constructor needed for initial values """
        self.my_initial = []
        if "course" in kwargs:
            course = kwargs['course']
            kwargs.pop("course")
            self.my_initial = map(lambda x: x.id, course.students.all())

        super(CourseForm, self).__init__(*args, **kwargs)
        self.fields['st'].initial = self.my_initial
