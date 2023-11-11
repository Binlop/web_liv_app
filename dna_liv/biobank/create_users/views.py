from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LabAdminForm, ProjectAdminForm, ProjectLabAssistantForm
from biobank.laboratory.models import Laboratory
from biobank.project.models import Project


@login_required
def create_lab_admin(request):
    if request.method == 'POST':
        form = LabAdminForm(request.POST)
        if form.is_valid():
            lab_name = form.cleaned_data['lab_name']
            lab = get_object_or_404(Laboratory, title=lab_name)
            lab_id = lab.id
            form.save()
            return redirect('single_laboratory', laboratory_id=lab_id)
    else:
        form = LabAdminForm()

    return render(request, 'biobank/create_users/create_lab_admin.html', {'form': form})


@login_required
def create_project_admin(request):
    if request.method == 'POST':
        form = ProjectAdminForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            project = get_object_or_404(Project, title=project_name)
            project_id = project.id
            form.save()
            return redirect('single_project', project_id=project_id)
    else:
        form = ProjectAdminForm()

    return render(request, 'biobank/create_users/create_project_admin.html', {'form': form})


@login_required
def create_project_assistant(request):
    if request.method == 'POST':
        form = ProjectLabAssistantForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            project = get_object_or_404(Project, title=project_name)
            project_id = project.id
            form.save()
            return redirect('single_project', project_id=project_id)
    else:
        form = ProjectLabAssistantForm()

    return render(request, 'biobank/create_users/create_lab_assistant.html', {'form': form})