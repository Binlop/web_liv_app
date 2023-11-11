from django.urls import path
from . import views

""""Отслеживаем переходы на разные ссылки и соответсвенно им выдаем представления"""

urlpatterns = [
    path('', views.list_laboratories, name='list_laboratories'),
    path('laboratory/laboratory<int:laboratory_id>/', views.single_laboratory, name='single_laboratory'), 
    path('create/', views.create_lab, name='create_lab'),
    path('laboratory/laboratory<int:laboratory_id>/update', views.LabUpdate.as_view(), name='lab_update'),
]