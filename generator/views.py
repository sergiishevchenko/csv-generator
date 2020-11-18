from django.shortcuts import render, redirect
from .models import SetSchema, NewSchema, Sets
from .forms import NewSchemaForm, SetSchemaForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from datetime import datetime
import csv

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
    context = {}
    SetFormset = modelformset_factory(SetSchema, form=SetSchemaForm)
    formset = SetFormset(request.POST or None, queryset=SetSchema.objects.none(), prefix='SetSchema')
    save_form = NewSchemaForm(request.POST)
    count = []
    if request.method == 'POST':
        if save_form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    new_schema = save_form.save(commit=False)
                    new_schema.user_id = request.user.id
                    new_schema.save()
                    for mark in formset:
                        data = mark.save(commit=False)
                        data.new_schema = new_schema
                        data.set_schema = save_form['schema_name'].value()
                        data.save()

                    sets = Sets()
                    sets.schema_name = save_form['schema_name'].value()
                    # sets.date -> str
                    sets.date = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")
                    sets.save()
            except IntegrityError:
                print("Error Encountered")
            return redirect('schemas')

    context['formset'] = formset
    context['form'] = save_form
    return render(request, 'new_schema.html', context)

def edit_schema(request, schema_name):
    sets_schema = Sets.objects.filter(schema_name=schema_name)
    row_list = []
    for item in list(SetSchema.objects.filter(set_schema=schema_name).values('column_name', 'column_type', 'column_order')):
        row_list.append(list(item.values()))

    new_schema_head = list(NewSchema.objects.filter(schema_name=schema_name).values('column_separator')[0].values())
    delimiter = new_schema_head[0]
    filename = schema_name + '_list.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(row_list)

    params = {'sets_schema': sets_schema}
    return render(request, 'edit_schema.html', params)

def generate_data(request):
    print(1)
    sets_schema = Sets.objects.all()
    params = {'sets_schema': sets_schema}
    return render(request, 'edit_schema.html', params)

def download(request):

    return redirect('edit_schema')

def del_schema(request, id):
    data_schemas = NewSchema.objects.filter(id=id)
    del_sets = SetSchema.objects.filter(set_schema=data_schemas[0].schema_name).delete()
    NewSchema.objects.filter(id=id).delete()
    return redirect('schemas')