from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm, CommentForm

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'add_exercise.html', {'form': form})

def add_comment(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.exercise = exercise
            comment.save()
            return redirect('flashcards')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'exercise': exercise})

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_list.html', {'exercises': exercises})

def flashcards(request):
    exercises = Exercise.objects.all()
    return render(request, 'flashcards.html', {'exercises': exercises})