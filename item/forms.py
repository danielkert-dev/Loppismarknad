from django import forms

from .models import Item, Status


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'location', 'status')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

        error_messages = {
            'category': {'required': ("Detta fält är obligatoriskt!")},
            'name': {'required': ("Detta fält är obligatoriskt!")},
            'description': {'required': ("Detta fält är obligatoriskt!")},
            'price': {'required': ("Detta fält är obligatoriskt!")},
            'location': {'required': ("Detta fält är obligatoriskt!")},
            'image': {'required': ("Detta fält är obligatoriskt!")},
            'status': {'required': ("Detta fält är obligatoriskt!")},
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'location', 'status')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control '}),
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

        error_messages = {
            'category': {'required': ("Detta fält är obligatoriskt!")},
            'name': {'required': ("Detta fält är obligatoriskt!")},
            'description': {'required': ("Detta fält är obligatoriskt!")},
            'price': {'required': ("Detta fält är obligatoriskt!")},
            'location': {'required': ("Detta fält är obligatoriskt!")},
            'image': {'required': ("Detta fält är obligatoriskt!")},
            'status': {'required': ("Detta fält är obligatoriskt!")},
        }