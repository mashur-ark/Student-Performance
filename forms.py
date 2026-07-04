from django import forms
from .models import Dataset


class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = [
            'dataset_name',
            'dataset_file',
            'description',
        ]

        widgets = {
            'dataset_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'dataset_file': forms.FileInput(attrs={
                'class': 'form-control'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
        }