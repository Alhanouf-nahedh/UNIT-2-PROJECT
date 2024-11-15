from django import forms
from dashboard.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'duration' ,'description']
