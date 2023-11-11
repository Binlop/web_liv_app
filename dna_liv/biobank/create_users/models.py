from django.db import models
from django.contrib.auth.models import User
from biobank.project.models import Project
from biobank.laboratory.models import Laboratory


# Админ лаборатории
class LabAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lab_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


# Админ проекта
class ProjectAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
    

# Лаборант проекта
class ProjectLabAssistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
