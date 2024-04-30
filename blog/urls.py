from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_create/',views.CreatePost.as_view(),
         name='post_create'),
    path('post_update/<slug:slug>',views.PostUpdate.as_view(),
         name='update_post'),
    path('delete_post/<slug:slug>',views.DeletePost.as_view(),
         name='delete_post'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('like/<slug:slug>', views.Like.as_view(),
         name='post_like'),
]