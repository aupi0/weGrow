from rest_framework import serializers
from django.contrib.auth.models import User

from .models import (
    WeGrowUser,
    FeedPost,
    TradePost,
    FeedPostComment,
    TradePostComment,
    FeedPostLike,
)

class WeGrowUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
    )
    feed_posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    #do not want to show password for obvious reasons, also not store in plain text
    class Meta:
        model = WeGrowUser
        fields = ('user', 'username', 'email', 'password', 'feed_posts')
    
    def create(self, validated_data):
        #create django user
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        #create WeGrowUser
        weGrowUser = WeGrowUser.objects.create(
            user = user,
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return weGrowUser


class FeedPostSerializer(serializers.ModelSerializer):
    #userID = serializers.ReadOnlyField(source = 'userID.username')
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #created_by = serializers.CurrentUserDefault()
    #alter model.save to commit=false
    #add current user to model, then save properly
    #get paramter within post_save signal

    class Meta:
        model = FeedPost
        fields = ('id', 'owner', 'plant_name', 'created', 'description', 'likes', 'comments')  

#TODO: need updating like feedPostSerializer
class TradePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePost
        fields = ('id', 'userID', 'feed_post', 'quantity', 'price',
            'currency', 'created', 'trade_description',
        )

class FeedPostCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = FeedPostComment
        fields = ('id', 'owner', 'feed_post', 'created', 'comment')

class TradePostCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = TradePostComment
        fields = ('id', 'owner', 'trade_post', 'created', 'comment')

class FeedPostLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = FeedPostLike
        fields = ('id', 'owner', 'feed_post')