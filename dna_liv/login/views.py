from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import RegistrationForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user=user)
            request.session['username'] = username  # Добавляем имя пользователя в сессию
            return redirect('home')
    return render(request, 'login/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('Проверка формы')
        print(form)
        if form.is_valid():
            print('Проходит регистрация')
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            print(f'Это новый user: {user}')
            if user is not None:
                login(request, user)
                print('Успешная регистрация и авторизация')
                request.session['username'] = username  # Добавляем имя пользователя в сессию
                # Пользователь успешно аутентифицирован
                return redirect('home')  # Здесь перенаправьте пользователя на вашу главную страницу
    else:
        form = RegistrationForm()
    return render(request, 'login/register.html', {'form': form})