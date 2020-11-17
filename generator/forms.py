from django import forms
from .models import NewSchema, SetSchema

class NewSchemaForm(forms.ModelForm):
    class Meta:
        model = NewSchema

        fields = [
            'schema_name',
            'column_separator',
            'string_character',
        ]

        labels = {
            'schema_name': 'schema_name',
            'column_separator': 'column_separator',
            'string_character': 'string_character',
        }

class SetSchemaForm(forms.ModelForm):
    class Meta:
        model = SetSchema

        fields = [
            'column_name',
            'column_type',
            'column_order',
        ]

        widgets = {
            'column_name': forms.TextInput(attrs={'class': 'formset-field'}),
            'column_type': forms.TextInput(attrs={'class': 'formset-field'}),
            'column_order': forms.TextInput(attrs={'class': 'formset-field'})
        }
