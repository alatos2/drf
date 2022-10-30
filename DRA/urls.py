from django.urls import path
from .views import PostsView, PostDetailsView

urlpatterns = [
    path('posts/', PostsView),
    path('details/<int:pk>/', PostDetailsView)
]