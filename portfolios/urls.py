from django.urls import path
from portfolios import views


urlpatterns = [
    path('', views.PhotosAPIView.as_view(), name='index'),
    path('portfolios/<int:pk>/', views.UserPortfoliosAPIView.as_view(), name='portfolios'),
    path('portfolio/<int:pk>/', views.PortfolioDetailAPIView.as_view(), name='portfolio'),
    path('addimage/', views.CreatePhotoAPIView.as_view(), name='add_image'),
    path('photo/<int:pk>/', views.PhotoDetailAPIView.as_view(), name='photo_detail'),
    path('createportfolio/', views.CreatePortfolioAPIView.as_view(), name='create_portfolio'),
]


