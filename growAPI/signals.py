from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (
    FeedPostLike,
    WeGrowUser,
    FeedPost,
    TradePost,
    FeedPostComment,
    TradePostComment,
)

@receiver(post_save, sender=FeedPostComment)
def notify_feed_post_author_comment(sender, instance, created, **kwargs):
    #runs if comment is newly created
    if created:
        print("newly created Feed post comment")
    else:
        print("edited Feed post comment")

@receiver(post_save, sender=TradePostComment)
def notify_trade_post_author_comment(sender, instance, created, **kwargs):
    #runs if comment is newly created
    if created:
        print("newly created Trade post comment")
    else:
        print("edited trade post comment")

@receiver(post_save, sender=FeedPostLike)
def notify_feed_post_author_like(sender, instance, created, **kwargs):
    #runs if comment is newly created
    if created:
        print(instance.user, " liked  the following post: ", instance.feed_post)
    else:
        print("should never be possible")