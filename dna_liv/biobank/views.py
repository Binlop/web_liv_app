from django.shortcuts import render
""""Представление различных разделов биобанка прописано здесь"""


# Отображение главной страницы
def biobank_home(request):
    data = {
        'title': 'Биобанк',
    }
    return render(request, 'biobank/index.html', data)


def permission_error(request):
    data = {
        'title': 'Биобанк',
    }
    return render(request, 'biobank/permission_error.html', data)