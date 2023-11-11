from django.db import models


# Create your models here.
# Создание отдельного класса для отдельной модели(таблицы) и прописывание полей(столбцов)
class Articles(models.Model): #Обязательное наследование разных типов полей
    # Указываем виджет поля, его название, кол-во символов в поле, значенеи по умолчанию
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    text = models.TextField('Текст', default='')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    # Для нормального отображения в панели администратора таблицы Новость в ед и мн.ч
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'