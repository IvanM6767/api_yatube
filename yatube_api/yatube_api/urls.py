from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'groups', GroupViewSet)
router_v1.register(r'posts', PostViewSet)
router_v1.register(
    r'posts/(?P<post>\d+)/comments', CommentViewSet, basename='comment'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_v1.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
