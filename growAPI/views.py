#from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import (
    viewsets,
    generics,
    permissions,
)

from .serializers import (
    WeGrowUserSerializer,
    FeedPostSerializer,
    TradePostSerializer,
    FeedPostCommentSerializer,
    TradePostCommentSerializer,
)
from .models import (
    WeGrowUser,
    FeedPost,
    TradePost,
    FeedPostComment,
    TradePostComment,
)
from .permissions import IsOwnerOrReadOnly

# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to WeGrow API.")

class growAPIView(viewsets.ModelViewSet):
    serializer_class = WeGrowUserSerializer
    queryset = WeGrowUser.objects.all()

class WeGrowUserCreateView(generics.CreateAPIView):
    queryset = WeGrowUser.objects.all()
    serializer_class = WeGrowUserSerializer

class WeGrowUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeGrowUser.objects.all()
    lookup_url_kwarg = 'username'
    serializer_class = WeGrowUserSerializer
    
#TODO:would need restricting/filtering to only friends
class FeedPostListView(generics.ListAPIView):
    queryset = FeedPost.objects.all()
    serializer_class = FeedPostSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FeedPostCreateView(generics.CreateAPIView):
    queryset = FeedPost.objects.all()
    serializer_class = FeedPostSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        weGrowUser = WeGrowUser.objects.get(user=self.request.user)
        serializer.save(owner=weGrowUser)

class FeedPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedPost.objects.all()
    #lookup_url_kwarg = 'username'
    serializer_class = FeedPostSerializer
    #permission_classes = [
    #    permissions.IsAuthenticatedOrReadOnly,
    #    IsOwnerOrReadOnly,
    #]
    
#TODO:would need restricting/filtering to distances or types of veg/fruit etc
class TradePostListView(generics.ListAPIView):
    queryset = TradePost.objects.all()
    serializer_class = TradePostSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TradePostCreateView(generics.CreateAPIView):
    queryset = TradePost.objects.all()
    serializer_class = TradePostSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
    #    serializer.save(owner = self.request.user)

class TradePostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradePost.objects.all()
    #lookup_url_kwarg = 'username'
    serializer_class = TradePostSerializer
    #permission_classes = [
    #    permissions.IsAuthenticatedOrReadOnly,
    #    IsOwnerOrReadOnly,
    #]

class FeedPostCommentListView(generics.ListAPIView):
    queryset = FeedPostComment.objects.all()
    serializer_class = FeedPostCommentSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FeedPostCommentCreateView(generics.CreateAPIView):
    queryset = FeedPostComment.objects.all()
    serializer_class = FeedPostCommentSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FeedPostCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedPostComment.objects.all()
    serializer_class = FeedPostCommentSerializer
    #permission_classes = [
    #    permissions.IsAuthenticatedOrReadOnly,
    #    IsOwnerOrReadOnly,
    #]

class TradePostCommentListView(generics.ListAPIView):
    queryset = TradePostComment.objects.all()
    serializer_class = TradePostCommentSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TradePostCommentCreateView(generics.CreateAPIView):
    queryset = TradePostComment.objects.all()
    serializer_class = TradePostCommentSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TradePostCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradePostComment.objects.all()
    serializer_class = TradePostCommentSerializer
    #permission_classes = [
    #    permissions.IsAuthenticatedOrReadOnly,
    #    IsOwnerOrReadOnly,
    #]