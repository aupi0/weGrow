from django.urls import path, re_path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'user', views.growAPIView)

urlpatterns = [
    path('', views.index, name='index'),
    path('router/', include(router.urls)),
    path('feed/', views.FeedPostListView.as_view()),
    path('feed/new/', views.FeedPostCreateView.as_view()),
    path('feed/<int:pk>/', views.FeedPostDetailView.as_view()),
    path('trade/', views.TradePostListView.as_view()),
    path('trade/new/', views.TradePostCreateView.as_view()),
    path('trade/<int:pk>/', views.TradePostDetailView.as_view()),
    path('feed/comments/', views.FeedPostCommentListView.as_view()),
    path('feed/comments/new/', views.FeedPostCommentCreateView.as_view()),
    path('feed/comment/<int:pk>/', views.FeedPostCommentDetailView.as_view()), # I hate this
    path('trade/comments/', views.TradePostCommentListView.as_view()),
    path('trade/comments/new/', views.TradePostCommentCreateView.as_view()),
    path('trade/comment/<int:pk>/', views.TradePostCommentDetailView.as_view()), # I hate this
    path('user/new/', views.WeGrowUserCreateView.as_view()),
    re_path(r'^user/(?P<username>[\w.@+-]+)/$', views.WeGrowUserDetailView.as_view()),
]