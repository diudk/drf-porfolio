from django.contrib.auth import logout
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, views

from .models import User
from .permissions import IsProfileOwnerOrReadOnly
from .serializers import UserLoginSerializer, UserSignupSerializer, UserSerializer


class UserSignupAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSignupSerializer
    http_method_names = ['post']


class UserLoginAPIView(views.APIView):
    permission_classes = (AllowAny, )
    serializer_class = UserLoginSerializer
    http_method_names = ['post']

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogoutAPIView(views.APIView):
    permission_classes = (IsAuthenticated, )
    http_method_names = ['get']

    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({
            'result': True,
        }, status=status.HTTP_200_OK)


class UserProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsProfileOwnerOrReadOnly, IsAuthenticated, )
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'delete', 'patch', ]
    queryset = User.objects.all()
