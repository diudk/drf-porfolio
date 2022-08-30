from django.http import JsonResponse
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.utils import custom_exception_handler
from .permissions import IsPhotoOwnerOrReadOnly, IsPortfolioOwnerOrReadOnly
from .models import Photo, Portfolio
from .serializers import PhotoSerializer, PortfolioSerializer


def error_404(request, exception):
    return JsonResponse(custom_exception_handler(exception, request).data)


class PhotosAPIView(generics.ListAPIView):
    search_fields = ['name', 'description', 'portfolio__name']
    filter_backends = (filters.SearchFilter,)
    permission_classes = (AllowAny, )
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    http_method_names = ['get']


class UserPortfoliosAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PortfolioSerializer
    search_fields = ['name', 'description']
    filter_backends = (filters.SearchFilter,)
    http_method_names = ['get']

    def get_queryset(self):
        return Portfolio.objects.filter(user_created=self.kwargs['pk'])


class CreatePortfolioAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PortfolioSerializer
    http_method_names = ['post']


class PortfolioDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPortfolioOwnerOrReadOnly, IsAuthenticated, )
    serializer_class = PortfolioSerializer
    http_method_names = ['get', 'put', 'delete', ]
    queryset = Portfolio.objects.all()


class CreatePhotoAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PhotoSerializer
    http_method_names = ['post']


class PhotoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPhotoOwnerOrReadOnly, IsAuthenticated, )
    serializer_class = PhotoSerializer
    http_method_names = ['get', 'put', 'delete', 'patch', ]
    queryset = Photo.objects.all()





