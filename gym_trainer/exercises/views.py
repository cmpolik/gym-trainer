"""
Views for the exercises app.
"""
from django.shortcuts import render, redirect
from exercises.models import Exercise
from exercises.forms import ExerciseForm, CommentForm

def home(request):
    """Display the homepage."""
    return render(request, 'home.html')

def add_exercise(request):
    """Add a new exercise."""
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'add_exercise.html', {'form': form})

def add_comment(request, exercise_id):
    """Add a comment to an exercise."""
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
    """Display a list of exercises with muscle filtering."""
    muscles = request.GET.get('muscles', '')
    exercises = Exercise.objects.all()
    if muscles:
        exercises = exercises.filter(muscles__icontains=muscles)
    return render(request, 'exercise_list.html', {'exercises': exercises, 'muscles': muscles})

def flashcards(request):
    """Display exercise flashcards."""
    exercises = Exercise.objects.all()
    return render(request, 'flashcards.html', {'exercises': exercises})

def upload_media(request, exercise_id):
    """Upload a media file for an exercise."""
    exercise = Exercise.objects.get(id=exercise_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    return redirect('exercise_list')