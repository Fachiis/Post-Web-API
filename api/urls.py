from django.urls import path

from .views import PostList, VoteCreate, PostRetrieveDestroy

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostRetrieveDestroy.as_view()),
    path('posts/<int:pk>/vote/', VoteCreate.as_view()),
]
