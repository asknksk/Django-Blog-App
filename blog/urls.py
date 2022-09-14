from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:id>/', views.blog_detail, name="post_detail"),
    path('add/', views.PostCreateView.as_view(),name='blog_add'),
]