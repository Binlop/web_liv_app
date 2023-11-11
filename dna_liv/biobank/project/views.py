from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator


def lab_admin_check(user):
    # Проверяем, является ли пользователь членом группы "лаборанты_проекта"
    return user.groups.filter(name='админы_лабы').exists()


@method_decorator(user_passes_test(lab_admin_check, login_url='permission_error'), name='dispatch')
class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'biobank/project/create_project.html'
    form_class = ProjectForm
    
    def get_object(self, queryset=None):
        form_id = self.kwargs['form_id']
        return Project.objects.get(pk=form_id)
    
    success_url = reverse_lazy('list_projects')


@login_required(login_url='permission_error')
def list_projects(request):
    
    projects = Project.objects.filter()[:10]
    return render(request, 'biobank/project/projects.html', {'projects': projects})


@login_required(login_url='permission_error')
def single_project(request, project_id):
    project = Project.objects.filter(id=project_id)[0]
    return render(request, 'biobank/project/project.html', {'project': project})


@user_passes_test(lab_admin_check, login_url='permission_error')
def create_project(request):
    error = ''
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        error = form.errors.items()
        if form.is_valid():
            project = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            laboratory_instance = form.cleaned_data['laboratory']
            project.laboratory = laboratory_instance
            project.save()
            return redirect('list_projects')
        else:
            error = 'Форма была неверной'
    
    form = ProjectForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/project/create_project.html', data)