from django.urls import path
from . import views


# Отслеживаем переход по разным ссылкам в разделе /
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts', views.contact, name='contacts')
]
