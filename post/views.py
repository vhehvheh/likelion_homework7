#from django.shortcuts import render
from .models import Post#model
from post.serializer import PostSerializer
#each status -> processing response
#import rest_framework에서 mixins, generics
#from rest_framework import mixins
#from rest_framework import generics

from rest_framework import viewsets
#@action 처리
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse#우리가 custom api를 작성해 직접 response하고 싶을 때
from post.pagination import myPagination
'''
from django.http import Http404 #get object or 404 직접 구현
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView#apiview를 상속 받음
'''


# Create your views here.(CBV)
'''
class PostList(APIView):#post obj(data)'s listview 역할(리스트를 보여주는 역할)
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)#to return queryset -> many=True
        return Response(serializer.data)#directly return response -> serializer.data

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):#각각의 객체에 pk값으로 접근해서 띄워 보여주는 역할(각각의 post를 보여주는 역할도 이와 같은 논리)
#이런 비슷한 논리가 반복-> 낭비임.불필요한 코드의 답습. =>코드의 낭비를 막기위해 상속을 통해 불필요한 중복을 제거 : mixin 사용(?)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):#특정 pk값의 객체를 가져옴.
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Post = self.get_object(pk)
        Post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
#api root : The default basic root view for DefaultRouter

#SnippetList : snippet's list를 보여주는 역할(listview)
"""
class PostList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):#불필요한 코드의 중복을 예방=>상속 사용.
    #generics.GenericAPIView에 있는 queryset, serializer_class 변수를 등록
    # (->상속받은 것. 부모C엔 None으로 지정되어 있어서 어떤 모델을 사용해 작성할지는 아직모름.so, 상속을 받을 때 우리가 직접 사용할 모델, serializer에 대해 초기화를 해줘야 함.)
    queryset = Post.objects.all()#snippet(=model) based
    serializer_class = PostSerializer#we will use SnippetSerializer class to serialize

#우리가 필요로 하는 http method들이 선언되어 있고, 이에 대한 return문이 한줄씩 써있음
#인자 : self, request, 가변인자(*args, **kwargs)#인자의 길이,개수 상관x 다 받는다는 뜻.
    # *args : keyword가 아닌 인자를 받고, **kwargs : keyword인자를 받음.

    def get(self, request, *args, **kwargs):#get()->return list()
        return self.list(request, *args, **kwargs)#ListModelMixin에서 상속받은 M. APIView의 get M와 비슷한 역할

    def post(self, request, *args, **kwargs):#post()->return create()
        return self.create(request, *args, **kwargs)#CreateModelMixin에서 상속받은 M. APIView의 post M와 비슷한 역할

#detailView
class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):#상속
    queryset = Post.objects.all()#사용할 model, serializer직접 등록
    serializer_class = PostSerializer
#사용할 http M 지정
    def get(self, request, *args, **kwargs):#get()-> retrieve() M 호출
        return self.retrieve(request, *args, **kwargs)#similar to detailview's get M

    def put(self, request, *args, **kwargs):#put()->return update()
        return self.update(request, *args, **kwargs)#// put M

    def delete(self, request, *args, **kwargs):#delete()->return destroy()
        return self.destroy(request, *args, **kwargs)#// delete M
"""
#generic class-based views
'''
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

#http M 코드들의 중복을 피하기 위해 ->ListCreateAPIView에서 미리 다 처리
#(list와 create를 묶어주는 역할. PostList에 있던 get, post가 그대로 정의되어 있고 상속받아야 될 것들도 자체 상속으로 처리.)

class SnippetList(generics.ListCreateAPIView):#상속받아 정의
    queryset = Snippet.objects.all()#mixins에서처럼 직접 등록해줘야함
    serializer_class = SnippetSerializer

#RetrieveUpdateDestroyAPIView만 상속받아 정의하면 전처럼 똑같은 기능을 구현가능.
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
'''
#ReadOnlyModelViewSet:mixin에서 상속받은, 사실 상 retrieve, list M를 묶어주는 역할
#특정 객체를 가져다 주고(retrieve), 객체들의 목록을 가져다 줌(list)=>특정 객체를 readonly할 수 있게 도와주는 viewset
#So, 1개의 view로 postview, postdetailview 모두 구현 가능.
"""
class PostViewSet(viewsets.ReadOnlyModelViewSet):#This viewset automatically provides `list` and `detail` actions.
#읽기 기능만 필요할 땐 이거만 사용하면 됨.
    queryset = Post.objects.all()
    serializer_class = PostSerializer

"""


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = myPagination
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]#action 수행 권한을 설정하는 C. 인증된 요청(소유자)에만 권한 부여.비인증->readonly
#중요한 부분!!
#@action : 장식자(decorator)
#viewset으로 crud 구현. viewset에 이를 제외한 나만의 custom api를 작성하고 싶을 때
#renderer_classes:커스텀 api의 response객체를 어떤 형식으로 randering할지 결정.
#@action(method=['post'])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):#custom api M. 
        #어떤 M 방식으로 처리되는지? default는 get!
        #Post = self.get_object()
        return HttpResponse('who are you!')
"""
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
"""
'''
source restvenv/Scripts/activate
ls > cd firstrest
python manage.py runserver
'''