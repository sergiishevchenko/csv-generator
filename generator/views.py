from django.shortcuts import render, redirect
from .models import SetSchema, NewSchema
from .forms import NewSchemaForm, SetSchemaForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError

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
            except IntegrityError:
                print("Error Encountered")
            return redirect('schemas')

    context['formset'] = formset
    context['form'] = save_form
    return render(request, 'new_schema.html', context)

def edit_schema(request):
    return render(request, 'edit_schema.html')

def del_schema(request, id):
    data_schemas = NewSchema.objects.filter(id=id)
    del_sets = SetSchema.objects.filter(set_schema=data_schemas[0].schema_name).delete()
    NewSchema.objects.filter(id=id).delete()
    params = {'data_schemas': data_schemas, 'del_sets': del_sets}
    return render(request, 'schemas.html', params)
