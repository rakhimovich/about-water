from apps.water.models import Articles
from django.forms import ModelForm, TextInput, Textarea

class Articlesform(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons','description']
        
        widgets = {
            "title": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название статьти'
            }),
            "anons": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Анонс статьти'
            }),
            "description": Textarea(attrs={
                'class': 'from-control',
                'placeholder': 'Описание статьти'
            }),
        }
