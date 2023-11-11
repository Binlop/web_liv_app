from django.db import models

# Create your models here.
class Laboratory(models.Model): #Обязательное наследование разных типов полей
    """Модель характеризует биологический образец, его поля и необходима для его регистрации в БД. Поля в дальнейшем будут расширяться"""
    # Указываем виджет поля, его название, кол-во символов в поле, значение по умолчанию
    title = models.CharField('Название лаборатории', max_length=50, default='')
    head_lab = models.CharField('Заведующий лабораторий', max_length=50, default='')
    test_field = models.CharField('Тестовое поле', max_length=250, default='')


    # Для корректного отображения в админ-панели
    def __str__(self):
        return str(self.title)

    # Неизвестно для чего
    def get_absolute_url(self):
        return f'/biobank/{self.id}'

    # Для нормального отображения в панели администратора таблицы Новость в ед и мн.ч
    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'