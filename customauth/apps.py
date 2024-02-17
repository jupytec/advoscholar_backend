from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customauth'

    def ready(self):
        import customauth.signals
        # included 2 lines below to pass lint test
        test = customauth.signals
        print(test)
