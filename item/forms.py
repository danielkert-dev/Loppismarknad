from django import forms

from .models import Item, Category, CategoryGroup
from django.contrib.auth.models import User

from location_field.forms.plain import PlainLocationField



class NewItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        request = kwargs.pop('request', None)  # Get the request object

        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [('', 'Välja kategory')] + list(self.fields['category'].choices)[1:]
        self.fields['category'].queryset = Category.objects.order_by('group__name', 'name')
        self.fields['status'].choices = [('', 'Välja status')] + list(self.fields['status'].choices)[1:]
        self.fields['location'].initial = '60.0963705598206,19.927439689636234'
        if request and request.user.is_authenticated:
            self.fields['contact_email'].initial = request.user.email

         # Get all category groups
        category_groups = CategoryGroup.objects.all()

        # Create a list of choices with the category groups as the top selections
        group_choices = [(group.id, group.name) for group in category_groups]

        # Append the category choices under each group
        for group in category_groups:
            category_choices = [(category.id, category.name) for category in group.categories.all()]
            group_choices.append(('group', {'label': group.name, 'choices': category_choices}))

        # Update the choices of the category field
        self.fields['category'].widget.choices = group_choices





    class Meta:
        model = Item
        fields = ('category', 'name', 'contact_number', 'contact_email', 'description', 'price', 'image', 'city', 'location', 'status')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control my-2'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control my-2'}),
            'name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control my-2'}),
            'city': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'location': PlainLocationField(
                based_fields=['city'],
                attrs={'class': 'form-control'},
                initial='60.0963705598206,19.927439689636234'
            ),
            'image': forms.FileInput(attrs={'class': 'form-control my-2', 'placeholder': 'Välj fil'}),
            'status': forms.Select(attrs={'class': 'form-control my-2'}),
        }

        error_messages = {
            'category': {'required': ("Detta fält är obligatoriskt!")},
            'contact_number': {'required': ("Detta fält är obligatoriskt!")},
            'contact_email': {'required': ("Detta fält är obligatoriskt!")},
            'name': {'required': ("Detta fält är obligatoriskt!")},
            'description': {'required': ("Detta fält är obligatoriskt!")},
            'price': {'required': ("Detta fält är obligatoriskt!")},
            'city': {'required': ("Detta fält är obligatoriskt!")},
            'location': {'required': ("Detta fält är obligatoriskt!")},
            'image': {'required': ("Detta fält är obligatoriskt!")},
            'status': {'required': ("Detta fält är obligatoriskt!")},
        }


class EditItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = [('', 'Välja kategory')] + list(self.fields['category'].choices)[1:]
        self.fields['category'].queryset = Category.objects.order_by('group__name', 'name')
        self.fields['status'].choices = [('', 'Välja status')] + list(self.fields['status'].choices)[1:]
        self.fields['location'].initial = '60.0963705598206,19.927439689636234'

  # Get all category groups
        category_groups = CategoryGroup.objects.all()

        # Create a list of choices with the category groups as the top selections
        group_choices = [(group.id, group.name) for group in category_groups]

        # Append the category choices under each group
        for group in category_groups:
            category_choices = [(category.id, category.name) for category in group.categories.all()]
            group_choices.append(('group', {'label': group.name, 'choices': category_choices}))

        # Update the choices of the category field
        self.fields['category'].widget.choices = group_choices



    class Meta:
        model = Item
        fields = ('category', 'name', 'contact_number', 'contact_email', 'description', 'price', 'image', 'city', 'location', 'status')

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control my-2'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control my-2'}),
            'name': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control my-2'}),
            'city': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'location': PlainLocationField(
                based_fields=['city'],
                attrs={'class': 'form-control'},
                initial='60.0963705598206,19.927439689636234'
            ),
            'image': forms.FileInput(attrs={'class': 'form-control my-2', 'placeholder': 'Välj fil'}),
            'status': forms.Select(attrs={'class': 'form-control my-2'}),
        }

        error_messages = {
            'category': {'required': ("Detta fält är obligatoriskt!")},
            'contact_number': {'required': ("Detta fält är obligatoriskt!")},
            'contact_email': {'required': ("Detta fält är obligatoriskt!")},
            'name': {'required': ("Detta fält är obligatoriskt!")},
            'description': {'required': ("Detta fält är obligatoriskt!")},
            'price': {'required': ("Detta fält är obligatoriskt!")},
            'city': {'required': ("Detta fält är obligatoriskt!")},
            'location': {'required': ("Detta fält är obligatoriskt!")},
            'image': {'required': ("Detta fält är obligatoriskt!")},
            'status': {'required': ("Detta fält är obligatoriskt!")},
        }