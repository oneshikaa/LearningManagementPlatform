from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Grade
from .forms import GradeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
@login_required
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades:list_grades')
    else:
        form = GradeForm()
    return render(request, 'grades/add_grade.html', {'form': form})

@login_required
def list_grades(request):
    grades = Grade.objects.all()
    return render(request, 'grades/list_grades.html', {'grades': grades})

@login_required
def update_grade(request, grade_id):
    grade = Grade.objects.get(pk=grade_id)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grades:list_grades')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grades/update_grade.html', {'form': form, 'grade': grade})

@login_required
def delete_grade(request,grade_id):
    grade = Grade.objects.get(pk=grade_id)
    grade.delete()
    return redirect('grades:list_grades')



