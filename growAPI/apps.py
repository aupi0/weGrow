from django.apps import AppConfig

class GrowapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'growAPI'

    def ready(self):
        from .signals import (
            notify_feed_post_author_comment,
            notify_trade_post_author_comment,
            notify_feed_post_author_like,
        )
