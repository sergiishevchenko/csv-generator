from django.shortcuts import render, redirect
from .models import DataSchemas
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
    data_schemas = DataSchemas.objects.filter(id=user_id)
    params = {
        'data_schemas': data_schemas
    }
    return render(request, 'schemas.html', params)

def new_schema(request):
    return render(request, 'new_schema.html')

def edit_schema(request):
    return render(request, 'edit_schema.html')
