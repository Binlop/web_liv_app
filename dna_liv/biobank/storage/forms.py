from .models import Freezer, Shelf, Box, SampleLocation
from django import forms


class FreezerForm(forms.ModelForm):
    class Meta:
        model = Freezer
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название морозилки", #Указываем название этого поля на странице

            }),
        }

class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название полки", #Указываем название этого поля на странице

            }),
        }

class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название коробки", #Указываем название этого поля на странице

            }),
        }
        
class SampleForm(forms.ModelForm):
    class Meta:
        model = SampleLocation
        fields = ['title', 'count_samples', 'count_rows', 'count_col']
        widgets = {
            'title': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название образцов", #Указываем название этого поля на странице

            }),
            'count_samples': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название коробки", #Указываем название этого поля на странице

            }),
            'count_rows': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название коробки", #Указываем название этого поля на странице

            }),
            'count_col': forms.TextInput(attrs={ #Указываем сам виджет, который будем использовать
                'class': 'form-control', #Указываем стиль отображения из boostrap
                'placeholder': "Название коробки", #Указываем название этого поля на странице

            }),
        }