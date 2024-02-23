from django.apps import AppConfig


class StorebackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'storebackend'

    def ready(self):
        """
        Импорт сигналов
        """
        import storebackend.signals
