from django.shortcuts import render, redirect
from .models import DataSchemas
from django.contrib.auth.forms import UserCreationForm


# def login(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             user_data = User()
#             user_data.email = login_form.data.get("email", None)
#             user_data.password = login_form.data.get("password", None)
#             user_data.save()
#             user = User.objects.filter(email=user_data.email, password=user_data.password).first()
#             if user is not None:
#                 request.session['user_id'] = user.id
#                 username = user.email
#                 return redirect('schemas')
#             return render(request, 'registration/login.html')
#         else:
#             return render(request, 'registration/login.html')
#     return render(request, 'registration/login.html')

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
