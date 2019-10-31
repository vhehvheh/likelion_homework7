#json-> 직렬화
from .models import UserPost, Album, Files
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):#model based
    author_name = serializers.ReadOnlyField(source='author.username')#author name-> read only!
    class Meta:
        model = UserPost
        fields = ('pk', 'title', 'body','author_name')
        #fields = '__all__'
        #write_only_fields = ('title',)

class AlbumSerializer(serializers.ModelSerializer):#model based
    author_name = serializers.ReadOnlyField(source='author.username')
    image= serializers.ImageField(use_url=True)#이미지가 잘 올라갔는지 확인->url이용

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')

class FilesSerializer(serializers.ModelSerializer):#model based
    author_name = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)#file 필드의 내용->url로 받겠음.
    class Meta:
        model = Files
        fields = ('pk', 'author_name', 'myfile', 'desc')
