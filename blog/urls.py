from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
   # url이 'blog/'로 끝났을 때 post_list 호출
   path('', views.post_list, name='post_list'),

   # url이 'post/<int:pk>/'로 끝났을 때 post_detail 호출
   path('post/<int:pk>/', views.post_detail, name='post_detail'),

   # url이 'post/new/'로 끝났을 때 post_new 호출
   path('post/new/', views.post_new, name='post_new'),

   # url이 'post/<int:pk>/edit/'로 끝났을 때 post_edit 호출
   path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

   # url이 'post/<pk>/delete/'로 끝났을 때 post_delete 호출
   path('post/<pk>/delete/', views.post_delete, name='post_delete'),
]

