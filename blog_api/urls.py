#from .views import PostList, PostDetail, AuthorPostList, PostListDetailFilter, CreatePost, EditPost, AdminPostDetail, DeletePost
from .views import PostList, AuthorPostList, PostListDetailFilter, AdminManagePost
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter()
router.register(r'admin/managepost', AdminManagePost, basename='managepost')
router.register('', PostList, basename='post')

urlpatterns = [
    path('author/', AuthorPostList.as_view(), name='authorpostlist'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    path('', include(router.urls)),    
]

# urlpatterns = [
#     path('posts/<slug>/', PostDetail.as_view(), name='detailcreate'),
#     path('author/', AuthorPostList.as_view(), name='authorpostlist'),
#     path('search/', PostListDetailFilter.as_view(), name='postsearch'),
#     path('', PostList.as_view(), name='listcreate'),
#     #Post Admin URLs
#     path('admin/create/', CreatePost.as_view(), name='createpost'),
#     path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='adminpostdetail'),
#     path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
#     path('admin/delete/<int:pk>', DeletePost.as_view(), name='deletepost'),    
# ]


#Routers
# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls