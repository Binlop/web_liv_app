from django.urls import path
from . import views

""""Отслеживаем переходы на разные ссылки и соответсвенно им выдаем представления"""

urlpatterns = [
    path('storage/', views.storage_view, name='storage_view'), #Главная страница хранилища, список морозильников
    path('storage/create', views.create_freezer, name='create_freezer'), #Создание морозильника
    path('storage/freezer_<int:freezer_id>/', views.freezer_view, name='freezer_view'), #Список ящиков в морозилке
    path('storage/freezer_<int:freezer_id>/create_shelf/', views.create_shelf, name='create_shelf'), #Создание ящика в морозилке
    path('storage/freezer_<int:freezer_id>/shelf_<int:shelf_id>/', views.shelf_view, name='shelf_view'), #Список коробок в ящике
    path('storage/freezer_<int:freezer_id>/shelf_<int:shelf_id>/create', views.create_box, name='create_box'), #Создание коробки в ящике
    path('storage/freezer_<int:freezer_id>/shelf_<int:shelf_id>/box_<int:box_id>', views.box_view, name='box_view'), #Список образцов в коробке
    path('storage/freezer_<int:freezer_id>/shelf_<int:shelf_id>/box_<int:box_id>/create', views.create_sample, name='create_sample'), #Создание карты образцов
]