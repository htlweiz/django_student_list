"""
At the moment most of the logic happens here in the views file
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Student
from .forms import StudentForm

# Create your views here.

def detail_helper(request, student):
    """
    detail helper function used by create and detail of existing student
    @param request the http request used
    @param student a student object can be a new student object for creation
    """
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.first_name = form.cleaned_data['first_name']
            student.sure_name = form.cleaned_data['sure_name']
            student.birth_date = form.cleaned_data['birth_date']
            student.save()
        return HttpResponseRedirect('/student/%d' % student.pk)

    form = StudentForm(initial={
        'first_name': student.first_name,
        'sure_name': student.sure_name,
        'birth_date': student.birth_date,
        })

    context = {
        'student': student,
        'form': form,
        }
    return render(request, 'student/detail.html', context)



def detail(request, student_id):
    """ stub calling detail helper with student object """
    student = get_object_or_404(Student, pk=student_id)
    return detail_helper(request, student)

def create(request):
    """ stub calling detail helper with new student object """
    student = Student()
    return detail_helper(request, student)

def delete(_request, student_id):
    """
    deleting a student
    @param the http request used
    @param student_id id of the student to be deleted
    """
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return HttpResponseRedirect('../')

def index(request):
    """
    view returning a list of all students
    """
    template = loader.get_template('student/list.html')
    context = {
        'students': Student.objects.order_by('sure_name', 'first_name')
        }
    return HttpResponse(template.render(context), request)
