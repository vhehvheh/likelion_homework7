from rest_framework.routers import DefaultRouter#format_suffix_patterns
from django.urls import path, include
from post import views
#rest framework -> router -> url
#router기반에서 작성.

router = DefaultRouter()#define router
router.register('post', views.PostViewSet)#register router

urlpatterns = [
    path('', include(router.urls))
]
    #('post/', views.PostList.as_view()),#decide url
    #('post/<int:pk>/', views.PostDetail.as_view()),
#urlpatterns = format_suffix_patterns(urlpatterns)
