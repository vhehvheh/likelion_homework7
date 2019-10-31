#from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
#from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
#from userpost.models import UserPost#model
from rest_framework import viewsets
from .models import UserPost, Album, Files
from .serializer import UserSerializer, AlbumSerializer, FilesSerializer

from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.
class UserPostViewSet(viewsets.ModelViewSet):
    #authentication_classes =[TokenAuthentication]#내가 적용하고 싶은 방식
    #python manage.py drf_create_token iu516 #iu516's token create
    #Generated token d6779597a580101526186e6341f1ed2c993440f1 for user iu516

    #permission_classes = [IsAdminUser]#logout->401 Unauthorized(x), empty queryset
    #user1/seoyeon12 user2/121212sy
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]#어떤 필터를 기반으로 검색을 진행할지
    search_fields = ('title','body')#어떤 칼럼(title)을 기반으로 검색할 건지
    
    def get_queryset(self):
        #여기서 쿼리셋 필터링같은 일들을 처리하고 마지막에 쿼리셋 리턴할 예정
        qs = super().get_queryset()
        #qs = qs.filter(author__id=1)
        #id = 1번 user에 대해 filter. qs.filter.exclude()도 같은 기능. 
        if (self.request.user.is_authenticated):
        #지금 만약 로그인되어있다면, 로그인 유저의 글만 필터. else면 비어있는 쿼리셋 리턴.
            qs = qs.filter(author=self.request.user)
        else:
            qs=qs.none()
        return qs
    def perform_create(self, serializer):#create M 기능
        serializer.save(author=self.request.user)#내가 직접 작성한 user를 자동저장.

#authentication(서비스에대해 내가 어느정도 권한이 있음을 알려주는 과정) & permission(서비스 동작에 대해 권한.view 호출 시 1번째로 체크)
#우리가 설정한 사용자에게만 권한&권리를 주도록 해야함.

class ImageViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


from rest_framework.response import Response
from rest_framework import status

class FileViewSet(viewsets.ModelViewSet):
    
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        serializers = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_404_BAD_REQUEST)
    #perser_class 지정
    #create() 오버라이딩
