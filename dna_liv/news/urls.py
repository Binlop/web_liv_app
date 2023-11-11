from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'), #Отслеживаем переход на директорию news
    path('create', views.news_create, name='news_create'), #Отслеживаем переход на директорию create
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
]
