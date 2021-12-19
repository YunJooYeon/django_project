from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    # url이 'bookmark/'로 끝났을 때 BookmarkListView 호출
    path('', BookmarkListView.as_view(), name='list'),

    # url이 'add/'로 끝났을 때 BookmarkCreateView 호출
    path('add/', BookmarkCreateView.as_view(), name='add'),

    # url이 'detail/'로 끝났을 때 BookmarkDetailView 호출
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),

    # url이 'update/'로 끝났을 때 BookmarkUpdateView 호출
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),

    # url이 'delete/'로 끝났을 때 BookmarkDeleteView 호출
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]
