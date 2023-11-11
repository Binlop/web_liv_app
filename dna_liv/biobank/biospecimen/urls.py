from django.urls import path
from . import views

""""Отслеживаем переходы на разные ссылки и соответсвенно им выдаем представления"""

urlpatterns = [
    path('', views.list_biospecimens, name='list_biospecimens'),
    path('create/', views.create_biospecimen, name='create_biospecimen'),
    path('biospecimen/sample_<int:biospecimen_id>/', views.single_biospecimen, name='single_biospecimen'), 
    path('biospecimen/sample_<int:biospecimen_id>/update', views.SampleUpdate.as_view(), name='sample_update'),
]