# В вашем приложении urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.processing_dna, name='dna-length'),
    path('add-properties/', views.dna_analysis, name='dna_analysis'),
    path('alignment/', views.upload_file, name='alignment'),
    
]
