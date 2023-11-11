from django.apps import AppConfig


class BiobankConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'biobank'


    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(self.create_user_groups, sender=self)


    def create_user_groups(self, **kwargs):
        from django.contrib.auth.models import Group
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.auth.models import Permission
        from biobank.create_users.models import LabAdmin, ProjectAdmin, ProjectLabAssistant
        from biobank.laboratory.models import Laboratory
        from biobank.project.models import Project
        from biobank.biospecimen.models import Biospecimen

        def assign_permissions(group, model_classes, permissions):
            for model_class in model_classes:
                content_type = ContentType.objects.get_for_model(model_class)

                for permission in permissions:
                    codename = f'{permission}_{model_class._meta.model_name}'
                    perm, created = Permission.objects.get_or_create(
                        codename=codename,
                        content_type=content_type,
                        name=f'Can {permission} {model_class._meta.verbose_name}',
                    )

                    group.permissions.add(perm)

        # Создаем группы
        lab_admin_group, created = Group.objects.get_or_create(name='админы_лабы')
        project_admin_group, created = Group.objects.get_or_create(name='админы_проекта')
        lab_assistant_group, created = Group.objects.get_or_create(name='лаборанты_проекта')

        # Назначаем разрешения для каждой группы
        assign_permissions(lab_admin_group, [Project, Biospecimen], ['add', 'change', 'delete', 'view'])
        assign_permissions(project_admin_group, [Biospecimen], ['add', 'change', 'delete', 'view'])
        assign_permissions(lab_assistant_group, [Project, Biospecimen], ['view'])

