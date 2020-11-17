from django.contrib import admin
from django.urls import path, include
from generator.views import home, schemas, new_schema, edit_schema, signup, del_schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('schemas/', schemas, name='schemas'),
    path('schemas/new_schema', new_schema, name='new_schema'),
    path('schemas/edit_schema', edit_schema, name='edit_schema'),
    path('schemas/<id>', del_schema, name='del_schema')
]
