from django.apps import AppConfig

class BlogPlatformAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blog_Platform_App'

    def ready(self):
        import Blog_Platform_App.signals
