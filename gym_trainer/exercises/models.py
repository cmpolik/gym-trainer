from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    muscles = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment for {self.exercise.name}"
