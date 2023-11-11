from django.urls import path
from . import views

""""Отслеживаем переходы на разные ссылки и соответсвенно им выдаем представления"""

urlpatterns = [
    path('lab_admin/', views.create_lab_admin, name='create_lab_admin'),
    path('project_admin/', views.create_project_admin, name='create_project_admin'),
    path('project_ass/', views.create_project_assistant, name='create_project_assistant'),
]