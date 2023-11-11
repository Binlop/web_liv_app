from .models import Project
from biobank.laboratory.models import Laboratory
from django import forms


# Создаем отдельный класс, который будет именно отображать модель Biospecimen на сайте
class ProjectForm(forms.ModelForm):
    laboratory = forms.ModelChoiceField(
        queryset=Laboratory.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Лаборатория",
        }))
    class Meta:
        model = Project #Наследуем модель из БД
        
        fields = ['title', 'test_field'] #Задаем необходимые поля на сайте, имена поля на сайте и в БД могут отличатья

        # Создаем словарь виджетов(полей), как они будут отображаться на странице
        widgets = {
            'title': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название образца", #Указываем название этого поля на странице
            }),
            'test_field': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Тестовое поле",
            }),
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['test_field'].required = False