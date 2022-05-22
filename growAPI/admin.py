from django.contrib import admin


from .models import (
    WeGrowUser,
    FeedPost,
    TradePost,
    FeedPostComment,
    TradePostComment,
)

class WeGrowUserAPIAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')

class FeedPostAPIAdmin(admin.ModelAdmin):
    list_display = ('owner', 'plant_name', 'created')

class TradePostAPIAdmin(admin.ModelAdmin):
    list_display = ('trade_description', 'quantity', 'created')#'feedID', 'quantity')

class FeedPostCommentAPIAdmin(admin.ModelAdmin):
    list_display = ('owner', 'feed_post', 'comment')

class TradePostCommentAPIAdmin(admin.ModelAdmin):
    list_display = ('owner', 'trade_post', 'comment')

# Register your models here.
admin.site.register(WeGrowUser, WeGrowUserAPIAdmin)
admin.site.register(FeedPost, FeedPostAPIAdmin)
admin.site.register(TradePost, TradePostAPIAdmin)
admin.site.register(FeedPostComment, FeedPostCommentAPIAdmin)
admin.site.register(TradePostComment, TradePostCommentAPIAdmin)