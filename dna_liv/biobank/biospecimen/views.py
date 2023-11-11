from django.shortcuts import render, redirect
from .models import Biospecimen
from biobank.storage.models import SampleLocation
from biobank.project.models import Project
from .forms import BiospecimenForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from biobank.create_users.models import LabAdmin, ProjectAdmin, ProjectLabAssistant


def biospec_access_edit_check(user):
    return user.groups.filter(name__in=['админы_лабы', 'админы_проекта']).exists()


def biospec_access_view_check(user):
    return user.groups.filter(name__in=['админы_лабы', 'админы_проекта', 'лаборанты_проекта']).exists()


@method_decorator(user_passes_test(biospec_access_edit_check, login_url='permission_error'), name='dispatch')
class SampleUpdate(UpdateView):
    model = Biospecimen
    template_name = 'biobank/biospecimen/create_biospecimen.html'
    form_class = BiospecimenForm
    
    def get_object(self, queryset=None):
        biospecimen_id = self.kwargs['biospecimen_id']
        return Biospecimen.objects.get(pk=biospecimen_id)
    

@login_required(login_url='permission_error')
def list_biospecimens(request):
    user = request.user
    user_group = user.groups.all()[0]
    print('Это группа юзеров: ', user_group)
    if str(user_group) == 'админы_лабы':
        user_profile = (
            LabAdmin.objects.filter(user=user).first()
        )
        print('Это админ лабы: ', user_profile)
        lab_id = user_profile.lab_id
        projects = Project.objects.filter(laboratory_id=lab_id)
        biospecimens = Biospecimen.objects.filter(project__in=projects)
    else:
        user_profile = (
            ProjectAdmin.objects.filter(user=user).first() or 
            ProjectLabAssistant.objects.filter(user=user).first()
        )
        project_id = user_profile.project_id
        biospecimens = Biospecimen.objects.filter(project_id=project_id)
    print('Это профиль юзера', user_profile)
    return render(request, 'biobank/biospecimen/biospecimens.html', {'biospecimens': biospecimens})


@login_required(login_url='permission_error')
def single_biospecimen(request, biospecimen_id):
    
    biospecimen = Biospecimen.objects.filter(id=biospecimen_id)[0]
    return render(request, 'biobank/biospecimen/biospecimen.html', {'biospecimen': biospecimen})


@user_passes_test(biospec_access_edit_check, login_url='permission_error')
def create_biospecimen(request):
    error = ''
    if request.method == 'POST':
        form = BiospecimenForm(request.POST, request.FILES)
        print(form.errors.items())
        if form.is_valid():
            biospecimen = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            biospecimen.file_name = str(request.FILES.get('file'))  # Получаем название файла
            project_instance = form.cleaned_data['project']
            print(project_instance)
            biospecimen.project = project_instance
            sample_storage_id = biospecimen.location_id
            location = SampleLocation.objects.get(id=sample_storage_id)
            biospecimen.name_storage_sample = location
            print(f'Это location {location}')
            location.state_location = 'Занято'  # Измените на нужное состояние
            biospecimen.save()  # Теперь сохраняем объект
            print('Это айди образца биологического', biospecimen.id)
            location.sample_id = biospecimen.id
            location.save()
            return redirect('list_biospecimens')
        else:
            error = 'Форма была неверной'
    form = BiospecimenForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/biospecimen/create_biospecimen.html', data)