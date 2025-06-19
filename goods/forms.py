# forms.py
from django import forms
from .models import Products, Tags

class ProductForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Введите теги через запятую")

    class Meta:
        model = Products
        fields = ['title', 'description', 'image', 'price', 'category', 'is_available', 'size', 'material', 'tags']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form__input'
        self.fields['description'].widget.attrs['class'] = 'form__input'
        self.fields['price'].widget.attrs['class'] = 'form__input'
        self.fields['category'].widget.attrs['class'] = 'form__input'
        self.fields['size'].widget.attrs['class'] = 'form__input'
        self.fields['material'].widget.attrs['class'] = 'form__input'
        self.fields['tags'].widget.attrs['class'] = 'form__input'

