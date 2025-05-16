"""
Forms for the exercises app.
"""
from django import forms
from exercises.models import Exercise, Comment

class ExerciseForm(forms.ModelForm):
    """
    Form for adding or editing exercises.
    """
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscles', 'media_file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'media_file': forms.ClearableFileInput(attrs={'accept': '.gif,.jpg,.png'}),
        }

    def clean_name(self):
        """Validate that name is not empty."""
        name = self.cleaned_data['name']
        if not name:
            raise forms.ValidationError("Name cannot be empty")
        return name

    def clean_description(self):
        """Validate that description is at least 10 characters."""
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters")
        return description

class CommentForm(forms.ModelForm):
    """
    Form for adding comments to exercises.
    """
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_text(self):
        """Validate that comment is not empty."""
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError("Comment cannot be empty")
        return text