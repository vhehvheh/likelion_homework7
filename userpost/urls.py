from rest_framework.routers import DefaultRouter
from django.urls import path, include
from userpost import views
#rest framework -> router -> url
#router기반에서 작성.

router = DefaultRouter()#define router
router.register('essay', views.UserPostViewSet)#register router
router.register('album', views.ImageViewSet)
router.register('files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]