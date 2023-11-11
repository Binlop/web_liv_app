from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from biobank.project.models import Project
from biobank.laboratory.models import Laboratory
from .models import LabAdmin, ProjectAdmin, ProjectLabAssistant


class LabAdminForm(UserCreationForm):
    lab_name = forms.ModelChoiceField(
        queryset=Laboratory.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Выберите лабораторию",
        }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Логин",
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Пароль",
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Повторите пароль",
            }),
        }
    
    error_messages = {
        'password_mismatch': "Пароли не совпадают.",
        'password_too_short': "Пароль должен содержать как минимум 8 символов.",
        'password_common': "Пароль не должен быть слишком простым и распространенным.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None


    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        profile, created = LabAdmin.objects.get_or_create(user=user)       
        selected_lab = self.cleaned_data['lab_name']
        profile.lab_id = selected_lab.id
        profile.save()
        group = Group.objects.get(name='админы_лабы')
        user.groups.add(group)
        return user
    

class ProjectAdminForm(UserCreationForm):
    project_name = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Выберите проект",
        }))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Логин",
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Пароль",
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Повторите пароль",
            }),
        }

    error_messages = {
        'password_mismatch': "Пароли не совпадают.",
        'password_too_short': "Пароль должен содержать как минимум 8 символов.",
        'password_common': "Пароль не должен быть слишком простым и распространенным.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        profile, created = ProjectAdmin.objects.get_or_create(user=user)       
        selected_project = self.cleaned_data['project_name']
        profile.project_id = selected_project.id
        profile.save()
        return user
    

class ProjectLabAssistantForm(UserCreationForm):
    project_name = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Выберите проект",
        }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Логин",
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Пароль",
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Повторите пароль",
            }),
        }
        
    error_messages = {
        'password_mismatch': "Пароли не совпадают.",
        'password_too_short': "Пароль должен содержать как минимум 8 символов.",
        'password_common': "Пароль не должен быть слишком простым и распространенным.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        profile, created = ProjectLabAssistant.objects.get_or_create(user=user)       
        selected_project = self.cleaned_data['project_name']
        profile.project_id = selected_project.id
        profile.save()
        group = Group.objects.get(name='лаборанты_проекта')
        user.groups.add(group)
        return user
