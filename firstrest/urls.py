from django.contrib import admin
from django.urls import path, include
from post  import urls
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    #path('userpost/', include('userpost.urls')),
    path('', include('userpost.urls')),
    path('api-auth/', include('rest_framework.urls')),#logout 기능
    #path('api-token-auth/', obtain_auth_token),#setting to get token

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)