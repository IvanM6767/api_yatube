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

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(PostViewSet, self).perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnlyPermissions]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post'))
        new_queryset = Comment.objects.filter(post=post)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('post')
        )

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(CommentViewSet, self).perform_destroy(instance)
