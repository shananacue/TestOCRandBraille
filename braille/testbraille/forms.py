from django import forms
from .models import Text

class TestForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('test', 'image')

        widgets = {
            'test': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Test Name goes Here'}),
            
        }