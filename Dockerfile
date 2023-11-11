# Используйте официальный образ Python 3 в качестве базового образа
FROM python:3
FROM continuumio/miniconda3

# Set working directory for the project
WORKDIR /app
 
COPY environment_bioinform_platform.yml .

# Create Conda environment from the YAML file
RUN conda env create -f environment_bioinform_platform.yml
 
# Override default shell and use bash
SHELL ["conda", "run", "-n", "env", "/bin/bash", "-c"]

# Копирование вашего Django проекта в контейнер
COPY dna_liv /app