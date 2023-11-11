from django.contrib import admin

# Register your models here.
from .models import Articles

# Регистриурем модель(таблицу) в панели админа для ее отображения
admin.site.register(Articles)