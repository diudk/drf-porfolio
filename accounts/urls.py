from django.urls import path

from .views import UserSignupAPIView, UserLoginAPIView, UserLogoutAPIView, UserProfileAPIView


urlpatterns = [
    path('signup/', UserSignupAPIView.as_view(), name='user_registration'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='user_profile'),
]
