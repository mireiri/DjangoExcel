from django import forms
from myapp.models import File


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'title', 'file')
