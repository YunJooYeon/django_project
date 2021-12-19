from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

# 북마크 리스트(list) 뷰
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

# 북마크 생성(create) 뷰
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:list')
    template_name_suffix = '_create'

# 북마크 상세(detail) 뷰
class BookmarkDetailView(DetailView):
    model = Bookmark

# 북마크 수정(update) 뷰
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

# 북마크 삭제(delete) 뷰
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')
    # urls.py에 path 함수에 정의된 이름이 'list'인 것과 연결
