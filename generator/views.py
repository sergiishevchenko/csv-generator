from django.shortcuts import render, redirect
from .models import SetSchema, NewSchema
from .forms import NewSchemaForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def schemas(request):
    user_id = request.user.id
    data_schemas = NewSchema.objects.filter(user_id=user_id)
    params = {'data_schemas': data_schemas}
    return render(request, 'schemas.html', params)

def new_schema(request):
    if request.method == 'POST':
        save_form = NewSchemaForm(request.POST)
        if save_form.is_valid():
            user_id = request.user.id
            schema = NewSchema()
            set_schema = SetSchema()
            schema.user_id = user_id
            schema.schema_name = save_form.data.get('schema_name', None)
            schema.column_separator = save_form.data.get('column_separator', None)
            schema.string_character = save_form.data.get('string_character', None)

            set_schema.column_name = save_form.data.get('column_name', None)
            set_schema.column_type = save_form.data.get('column_type', None)
            set_schema.column_order = save_form.data.get('column_order', None)

            schema.save()
            set_schema.save()

            return redirect('schemas')
    return render(request, 'new_schema.html')

def edit_schema(request):
    return render(request, 'edit_schema.html')

def del_schema(request, id):
    NewSchema.objects.filter(id=id).delete()
    user_id = request.user.id
    data_schemas = NewSchema.objects.filter(user_id=user_id)
    params = {'data_schemas': data_schemas}
    return render(request, 'schemas.html', params)
