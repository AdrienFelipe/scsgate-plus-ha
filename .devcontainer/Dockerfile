FROM mcr.microsoft.com/devcontainers/python:3.11

# Mise à jour pip
RUN pip install --upgrade pip

# Installation des dépendances de test
COPY requirements_test.txt /tmp/requirements_test.txt
RUN pip install -r /tmp/requirements_test.txt
