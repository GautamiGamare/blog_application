from django.urls import path
from blog_app.views import *

urlpatterns = [
    path('posts/', posts_list.as_view()),
    path('posts/<pk>', posts_list.as_view()),
    path('post_update/',posts_update.as_view()),
    path('comments/', comments_list.as_view()),
    path('comments_create/',comments_create.as_view())
]
