from django.shortcuts import render
from .utils.processing_dna import ProcessingDna
from .forms import DNAAnalysisForm, UploadFileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from.models import MyFiles
from django.contrib.auth.models import User

def processing_dna(request):
    return render(request, "Processing_DNA/index.html")


def dna_analysis(request):
    if request.method == "POST":
        form = DNAAnalysisForm(request.POST)
        if form.is_valid():
            dna_sequence = form.cleaned_data["dna_sequence"]
            selected_properties = form.cleaned_data["properties"]
            processing_dna = ProcessingDna(
                dna_sequence, selected_properties
            )  # Создаем объект класса
            result = processing_dna.performing_functions()
            return render(
                request,
                "Processing_DNA/dna_analysis.html",
                {"form": form, "result": result},
            )
    else:
        form = DNAAnalysisForm()

    return render(request, "Processing_DNA/dna_analysis.html", {"form": form})



# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file


def upload_file(request):
    username = request.session.get('username', None)
    user = User.objects.filter(username=username).first()
    
    if user:
        user_files = MyFiles.objects.filter(user=user)
    else:
        user_files = None

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            MyFiles.objects.create(
                text = str(request.FILES.get('file')),
                file = request.FILES.get('file'),
                user = user
            )
            # handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect(reverse('dna-length'))
    else:
        form = UploadFileForm()
    return render(request, "Processing_DNA/alignment.html", {"form": form, 'all_files': user_files})
