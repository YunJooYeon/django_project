from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# 블로그 생성(new) 뷰
def post_list(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    # 조회
    posts = Post.objects.order_by('-create_date') # 최신 순으로 변경
    # 페이징처리
    paginator = Paginator(posts, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'posts': page_obj}
    return render(request, 'blog/post_list.html', context)

# 블로그 상세(detail) 뷰
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 블로그 생성(new) 뷰
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return  render(request, 'blog/post_edit.html', {'form':form})

# 블로그 수정(edit) 뷰
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form':form})

# 블로그 삭제(delete) 뷰
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')
