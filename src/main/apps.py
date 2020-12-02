from django.apps import AppConfig

# Set Created Application as if it was a Main Folder/ Class
# Importable through the INSTALLED_APPS List through settings.py
class MainConfig(AppConfig):
    name = 'main'
