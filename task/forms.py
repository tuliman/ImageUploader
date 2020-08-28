from django import forms
from .models import Images, Size
from django.core.exceptions import ValidationError


class ImageForm(forms.Form):
    image = forms.ImageField(label="Картинка", required=False)
    url = forms.URLField(label='Введите урл', required=False)


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        exclude = ('img',)
