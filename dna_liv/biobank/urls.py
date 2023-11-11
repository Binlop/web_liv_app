from django.urls import path, include
from . import views

""""Отслеживаем переходы на разные ссылки и соответсвенно им выдаем представления"""

urlpatterns = [
    path('', views.biobank_home, name='biobank_home'),
    path('permission_error', views.permission_error, name='permission_error'),
    path('biospecimen/', include('biobank.biospecimen.urls')),
    path('storage/', include('biobank.storage.urls')),
    path('laboratory/', include('biobank.laboratory.urls')),
    path('project/', include('biobank.project.urls')),
    path('create_users/', include('biobank.create_users.urls')),
]