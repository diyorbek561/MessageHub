from django.urls import path
from .views import PostCreateView, PostListView

urlpatterns = [
    path('', PostCreateView.as_view(), name='form'),
    path('xabarlar/', PostListView.as_view(), name='xabarlar'),
]