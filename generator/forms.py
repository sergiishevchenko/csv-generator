from django import forms

class NewSchemaForm(forms.Form):
    schema_name = forms.CharField(max_length=150)
    column_separator = forms.CharField(max_length=150)
    string_character = forms.CharField(max_length=150)
    column_name = forms.CharField(max_length=150)
    column_type = forms.CharField(max_length=150)
    column_order = forms.CharField(max_length=150)
