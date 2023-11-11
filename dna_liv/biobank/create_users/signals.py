from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import LabAdmin, ProjectAdmin, ProjectLabAssistant

@receiver(post_save, sender=User)
def create_lab_admin(sender, instance, created, **kwargs):
    if created:
        LabAdmin.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_project_admin(sender, instance, created, **kwargs):
    if created:
        ProjectAdmin.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_lab_assistant(sender, instance, created, **kwargs):
    if created:
        ProjectLabAssistant.objects.create(user=instance)
