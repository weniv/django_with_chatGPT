from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, CommentForm


def post_list_view(request):
    # 포스트 목록 뷰
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail_view(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user  # 현재 로그인한 사용자를 댓글의 작성자로 설정
            comment.save()
            return redirect("blog:post_detail", id=post.id)
    else:
        comment_form = CommentForm()

    return render(
        request, "blog/post_detail.html", {"post": post, "comment_form": comment_form}
    )


@login_required
def post_create_view(request):
    # 포스트 생성 뷰
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:post_detail", id=post.id)
    else:
        form = PostForm()
    return render(request, "blog/post_create.html", {"form": form})


@login_required
def post_edit_view(request, id):
    # 포스트 수정 뷰
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:post_detail", id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form, "post": post})


@login_required
def post_delete_view(request, id):
    # 포스트 삭제 뷰
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("blog:post_list")
