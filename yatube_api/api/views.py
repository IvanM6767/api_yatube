from django.core.exceptions import PermissionDenied
from posts.models import Comment, Group, Post
from rest_framework import viewsets
from .permissions import AuthorOrReadOnlyPermissions
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from django.shortcuts import get_object_or_404


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnlyPermissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnlyPermissions]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post'))
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post'))
        serializer.save(author=self.request.user, post_id=post.id)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(instance)
