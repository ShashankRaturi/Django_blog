from django.apps import AppConfig


class BlogUsersAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_users_app'

    def ready(self):
        import blog_users_app.signals
