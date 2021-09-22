from .views import PostList, PostDetail, AuthorPostList, PostListDetailFilter
from django.urls import path
#from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

urlpatterns = [
    path('posts/<slug>/', PostDetail.as_view(), name='detailcreate'),
    path('author/', AuthorPostList.as_view(), name='authorpostlist'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]


#Routers
# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls