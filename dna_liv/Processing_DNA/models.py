from django.db import models
from django.contrib.auth.models import User  # Импортируем модель User


# Create your models here.
class MyFiles(models.Model):
    text = models.CharField(max_length=50)
    file = models.FileField(upload_to = 'upldfile/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)