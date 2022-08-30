from django.urls import path

from .views import AddCommentToPhoto


urlpatterns = [
    path('addcomment/', AddCommentToPhoto.as_view(), name='add_comment'),
]
