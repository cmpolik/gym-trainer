"""
Models for the exercises app.
"""
from django.db import models

class Exercise(models.Model):
    """
    Model for storing gym exercises.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    muscles = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    media_file = models.FileField(upload_to='exercise_media/', blank=True, null=True)

    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    """
    Model for storing comments on exercises.
    """
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment for {self.exercise.name}"