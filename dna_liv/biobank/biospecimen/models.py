from django.db import models
from biobank.project.models import Project
from biobank.storage.models import SampleLocation

# Create your models here.
class Biospecimen(models.Model): #Обязательное наследование разных типов полей
    """Модель характеризует биологический образец, его поля и необходима для его регистрации в БД. Поля в дальнейшем будут расширяться"""
    # Указываем виджет поля, его название, кол-во символов в поле, значение по умолчанию
    title = models.CharField('Название образца', max_length=50, default='')
    test_field = models.CharField('Тестовое поле', max_length=250, default='')
    date = models.DateTimeField('Дата получения')
    file_name = models.CharField('Название файла', max_length=55)
    file = models.FileField(upload_to = 'upldfile/')
    name_storage_sample = models.CharField('Место хранения образца в хранилище', max_length=100, default='')
    location = models.ForeignKey(SampleLocation, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # Для корректного отображения в админ-панели
    def __str__(self):
        return str(self.title)

    # Неизвестно для чего
    def get_absolute_url(self):
        return f'/biobank/{self.id}'

    # Для нормального отображения в панели администратора таблицы Новость в ед и мн.ч
    class Meta:
        verbose_name = 'Биологический образец'
        verbose_name_plural = 'Биологические образцы'