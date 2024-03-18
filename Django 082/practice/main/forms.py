from .models import Position
from django.forms import ModelForm, TextInput, Textarea


class PosForm(ModelForm):
    class Meta:
        model = Position
        fields = ["name", "type", "price"]
        widgets = {
            "name": TextInput(attrs={'placeholder': 'Название', 'class': 'form-input'}),
            "type": TextInput(attrs={'placeholder': 'Производитель', 'class': 'form-input'}),
            "price": TextInput(attrs={'placeholder': 'Цена в руб.', 'class': 'form-input'}),
        }