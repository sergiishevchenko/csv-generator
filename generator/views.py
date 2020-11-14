from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User, DataSchemas
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_data = User()
            user_data.email = login_form.data.get("email", None)
            user_data.password = login_form.data.get("password", None)
            user_data.save()
            user = User.objects.filter(email=user_data.email, password=user_data.password).first()
            if user is not None:
                request.session['user_id'] = user.id
                return redirect('schemas')
            return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def schemas(request):
    user_id = request.session.get('user_id', None)
    data_schemas = DataSchemas.objects.filter(user_id=user_id)
    params = {
        'data_schemas': data_schemas
    }
    return render(request, 'schemas.html', params)

def new_schema(request):
    return render(request, 'new_schema.html')
