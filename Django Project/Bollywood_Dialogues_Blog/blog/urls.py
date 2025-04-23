from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),# Home page with all posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),# Individual post page
]