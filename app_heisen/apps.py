from django.apps import AppConfig


class AppHeisenConfig(AppConfig):
    name = 'app_heisen'
    def ready(self):
        import app_heisen.signals
