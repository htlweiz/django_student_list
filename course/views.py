from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django import forms

from .models import Course
from .forms import CourseForm


#
def detail_helper(request, course):
    """
    detail helper function used by create and detail of existing course 
    @param request the http request used
    @param course a course object can be a new course object for creation
    """
    form = CourseForm(course=course)

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course.course_name = form.cleaned_data['course_name']
            course.ects = form.cleaned_data['ects']
            course.students.set(form.cleaned_data['st'])
            course.save()
        return HttpResponseRedirect('/course/%d' % course.pk)
    form_initial = {
        'course_name': course.course_name,
        'ects': course.ects,
        }
    form = CourseForm(course=course,initial=form_initial)

    context = {
        'course': course,
        'form': form,
        }

    return render(request, 'course/detail.html', context)


def detail(request, course_id):
    """ stub calling detail helper with course """
    course = get_object_or_404(Course, pk=course_id)
    return detail_helper(request, course)
