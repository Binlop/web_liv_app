from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView #Динамически изменяемый url адрес

# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('-date')[:5] #Создаем объект новостей из базы данных и сортировка записей по дате(самые новые сверху)
    return render(request, 'news/index.html', {'news':news}) #Отправляем объекты новостей на сайт


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'


def news_create(request):
    error = ''
    if request.method == 'POST': #Проверяем, что данные из формы были отправлены с помощью метода POST
        form = ArticlesForm(request.POST) #Создаем переменную на основе объекта из формы
        if form.is_valid(): #Проверяем соответствие полей типам данных и сохраняем форму в БД
            form.save()
            return redirect('home') #После сохранения переносим пользователя на домашнюю страницу
        else:
            error = 'Форма была неверной'

    form = ArticlesForm #Создаем форму на основе модели(таблицы) в БД

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)  #Отправка формы или ошибки на страницу содания новости