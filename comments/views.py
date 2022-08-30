from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import CommentSerializer


class AddCommentToPhoto(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = CommentSerializer
    http_method_names = ['post']
