from .models import Biospecimen
from biobank.storage.models import SampleLocation
from biobank.project.models import Project
from django import forms

# Создаем отдельный класс, который будет именно отображать модель Biospecimen на сайте
class BiospecimenForm(forms.ModelForm):
    location = forms.ModelChoiceField(
        queryset=SampleLocation.objects.filter(state_location='free'),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Место хранения образца",
        }))
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': "Проект",
        }))
    class Meta:
        model = Biospecimen #Наследуем модель из БД
        
        fields = ['title', 'test_field', 'location', 'date', 'file'] #Задаем необходимые поля на сайте, имена поля на сайте и в БД могут отличатья

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
            'date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': "Ваш файл"
            }),
        }
    def __init__(self, *args, **kwargs):
        super(BiospecimenForm, self).__init__(*args, **kwargs)
        self.fields['test_field'].required = False