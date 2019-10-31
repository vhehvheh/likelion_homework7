from rest_framework.pagination import PageNumberPagination

class myPagination(PageNumberPagination):
    page_size = 2
#filtering(request 걸러보내기) & search(response 걸러받기)