from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea #Импорт необходимых виджетов

# Создаем отдельный класс, который будет именно отображать модель Articles на сайте
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles #Наследуем модель из БД
        fields = ['title', 'anons', 'text', 'date'] #Задаем необходимые поля на сайте, поля на сайте и БД могут отличатья

        # Создаем словарь виджетов(полей), как они будут отображаться на странице
        widgets = {
            'title': TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название статьи", #Указываем название этого поля на странице

            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс",

            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Текст статьи",

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата публикации"
            })
        }