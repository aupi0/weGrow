from django.db import models
from django.contrib.auth.models import User

class WeGrowUser(models.Model):
    #django_user = models.OneToOneField('auth.User', related_name='we_grow_user', on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='we_grow_user', on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

#TODO: friends?

#TODO: location need adding
#TODO: add pictures
class FeedPost(models.Model):
    plant_name = models.CharField(max_length=120, default='')
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='')
    #userID = models.ForeignKey(User, related_name='feed_posts', on_delete=models.CASCADE)
    owner = models.ForeignKey(WeGrowUser, related_name='feed_posts', on_delete=models.CASCADE)#SET_NULL?

    class Meta:
        ordering = ['created']

    def _str_(self):
        return self.plantName, " ", self.description

#TODO: location need adding
class TradePost(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # checks may be needed elsewhere for this e,g, is KG or lbs or numbered quantity
    quantity = models.CharField(max_length=30) 
    price = models.CharField(max_length=10)
    currency = models.CharField(max_length=30)
    trade_description = models.TextField()
    feed_post = models.ForeignKey(
        FeedPost,
        related_name='trade_posts',
        on_delete=models.CASCADE,
        null=True,
    )
    #user = models.ForeignKey(User.username, related_name='TradePosts', on_delete=models.CASCADE)
    userID = models.ForeignKey('auth.User', related_name='trade_posts', on_delete=models.CASCADE)

class FeedPostComment(models.Model):
    owner = models.ForeignKey(WeGrowUser, related_name='feed_post_comments', on_delete=models.CASCADE)
    feed_post = models.ForeignKey(FeedPost, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=250)

    class Meta:
        verbose_name_plural = 'FeedPostComments'

class TradePostComment(models.Model):
    owner = models.ForeignKey(WeGrowUser, related_name='trade_post_comments', on_delete=models.CASCADE)
    trade_post = models.ForeignKey(TradePost, related_name='comments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=250)

    class Meta:
        verbose_name_plural = 'TradePostComments'

class FeedPostLike(models.Model):
    owner = models.ForeignKey(WeGrowUser, related_name='feed_post_likes', on_delete=models.CASCADE)
    feed_post = models.ForeignKey(FeedPost, related_name='likes', on_delete=models.CASCADE)

#TODO: directMessages