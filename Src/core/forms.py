# core/forms.py
from django import forms
from .models import Task, Category, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'category', 'tags']

    title = forms.CharField(
        label='Title',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )

    due_date = forms.DateField(
        label='Due Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    status = forms.ChoiceField(
        label='Status',
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    category = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False  
    )

    tags = forms.ModelMultipleChoiceField(
        label='Tags',
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )
