from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Laboratory
from .forms import LabForm
from django.views.generic import UpdateView, DeleteView


class LabUpdate(UpdateView):
    model = Laboratory
    template_name = 'biobank/laboratory/create_laboratory.html'
    form_class = LabForm
    
    def get_object(self, queryset=None):
        lab_id = self.kwargs['laboratory_id']
        return Laboratory.objects.get(pk=lab_id)
    
    success_url = reverse_lazy('list_laboratories')


def list_laboratories(request):
    labs = Laboratory.objects.filter()[:10]
    return render(request, 'biobank/laboratory/laboratories.html', {'labs': labs})


def single_laboratory(request, laboratory_id):
    laboratory = Laboratory.objects.filter(id=laboratory_id)[0]
    return render(request, 'biobank/laboratory/laboratory.html', {'laboratory': laboratory})


def create_lab(request):
    error = ''
    if request.method == 'POST':
        form = LabForm(request.POST, request.FILES)
        print(form.errors.items())
        if form.is_valid():
            lab = form.save(commit=False)  # Создаем объект, но не сохраняем его в базе данных пока
            lab.save()
            return redirect('list_laboratories')
        else:
            error = 'Форма была неверной'
    form = LabForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'biobank/laboratory/create_laboratory.html', data)