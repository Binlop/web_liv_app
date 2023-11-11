from django.urls import path
from . import views

""""Отслеживаем переходы на разные ссылки и соответсвенно им выдаем представления"""

urlpatterns = [
    path('', views.list_projects, name='list_projects'),
    path('create/', views.create_project, name='create_project'),
    path('project/project<int:project_id>/', views.single_project, name='single_project'), 
    path('project/project<int:project_id>/update', views.ProjectUpdate.as_view(), name='project_update'),
]