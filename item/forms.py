from django import forms

from .models import Item
from location_field.forms.plain import PlainLocationField


class NewItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [('', 'Välja kategory')] + list(self.fields['category'].choices)[1:]

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'city', 'location', 'status')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control my-2'}),
            'name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder':'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control my-2'}),
            'city': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'location': PlainLocationField(based_fields=['city'], zoom=0,  initial='60.102196,19.942281' , attrs={'class': 'form-control my-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control my-2'}),
            'status': forms.Select(attrs={'class': 'form-control my-2'}),
        }

        error_messages = {
            'category': {'required': ("Detta fält är obligatoriskt!")},
            'name': {'required': ("Detta fält är obligatoriskt!")},
            'description': {'required': ("Detta fält är obligatoriskt!")},
            'price': {'required': ("Detta fält är obligatoriskt!")},
            'city': {'required': ("Detta fält är obligatoriskt!")},
            'location': {'required': ("Detta fält är obligatoriskt!")},
            'image': {'required': ("Detta fält är obligatoriskt!")},
            'status': {'required': ("Detta fält är obligatoriskt!")},
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'city', 'location', 'status')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control my-2'}),
            'name': forms.TextInput(attrs={'class': 'form-control my-2',}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control my-2'}),
            'city': forms.TextInput(attrs={'class': 'form-control my-2',}),
            'location': PlainLocationField(based_fields=['city'], zoom=0, initial='60.102196,19.942281', attrs={'class': 'form-control my-2'}),
            'image': forms.FileInput(attrs={'class': 'form-control my-2'}),
            'status': forms.Select(attrs={'class': 'form-control my-2'}),
        }

        error_messages = {
            'category': {'required': ("Detta fält är obligatoriskt!")},
            'name': {'required': ("Detta fält är obligatoriskt!")},
            'description': {'required': ("Detta fält är obligatoriskt!")},
            'price': {'required': ("Detta fält är obligatoriskt!")},
            'city': {'required': ("Detta fält är obligatoriskt!")},
            'location': {'required': ("Detta fält är obligatoriskt!")},
            'image': {'required': ("Detta fält är obligatoriskt!")},
            'status': {'required': ("Detta fält är obligatoriskt!")},
        }