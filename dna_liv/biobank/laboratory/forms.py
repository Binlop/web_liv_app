from .models import Laboratory
from django import forms


# Создаем отдельный класс, который будет именно отображать модель Biospecimen на сайте
class LabForm(forms.ModelForm):
    class Meta:
        model = Laboratory #Наследуем модель из БД
        
        fields = ['title', 'head_lab', 'test_field'] #Задаем необходимые поля на сайте, имена поля на сайте и в БД могут отличатья

        # Создаем словарь виджетов(полей), как они будут отображаться на странице
        widgets = {
            'title': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название образца", #Указываем название этого поля на странице
            }),
            'head_lab': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Заведующий отделом",
            }),
            'test_field': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Тестовое поле",
            }),
        }
    def __init__(self, *args, **kwargs):
        super(LabForm, self).__init__(*args, **kwargs)
        self.fields['head_lab'].required = False