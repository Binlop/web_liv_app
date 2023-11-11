from django.shortcuts import render


def index(request):
    print(request.GET)
    username = request.session.get('username', None)
    print(f'Текущий пользователь: {username}')
    # username = (request.POST.dict())['username']
    # Создание тестового словаря для вывода его значений на главную страницу сайта
    print('Рендерится главная страница')
    data = {'title': 'Главная страница',
            'username': username
            }
    # print(request.user.username)
    return render(request, 'main/index.html', data) # Добавлям объект, который отправляем


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')