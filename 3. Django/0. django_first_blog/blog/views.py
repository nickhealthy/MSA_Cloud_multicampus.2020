from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostModelForm, PostForm, CommentModelForm


# Comment 승인
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


# Comment 삭제
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

# Comment 등록
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # form 객체생성
        form = CommentModelForm(request.POST)
        # form valid check
        if form.is_valid():
            # author, text 값이 comment 객체에 저장
            comment = form.save(commit=False)
            # Comment 객체에 매칭되는 post id를 저장
            comment.post = post
            # DB에 저장
            comment.save()
            # 문제가 없으면 실제로 return 해서 뿌린다.
            return redirect('post_detail', pk=post.pk)
    else:
        # Form.py 에 등록한 class 를 추가
        form = CommentModelForm()
    # 문제가 있든 없든 >> 통신요청 >> html 템플릿을 뿌려주고 >> {'form': form} = CommentModelForm() class 를 뿌려준다.
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# Post 삭제
@login_required
def post_remove(requests, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


# Post 수정
@login_required
def post_edit(request, pk):
    # DB 에서 해당 pk와 매칭되는 Post 객체를 가져온다.
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        # 수정처리 / PostModelForm 사용
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user.username)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # 수정하기 전에 데이터를 읽어온다.
        # PostModelForm << class / instance=post 14번째 줄 있는 객체 가져온다.
        form = PostModelForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# Post 등록
# 로그인이 안되어 있으면 안되게 하는 체크를 해주는 데코레이터
@login_required
def post_new(request):
    if request.method == 'POST':
        # Form 데이터를 입력하고 등록요청 했을때 (save) / PostForm 사용
        form = PostForm(request.POST)
        # Form 데이터가 clean 한 상태
        if form.is_valid():
            print(form.cleaned_data)
            # Form 은 QuerySet 을 함수를 이용 해야한다.
            post = Post.objects.create(author=User.objects.get(username=request.user.username),
                                       published_date=timezone.now(),
                                       title=form.cleaned_data['title'],
                                       text=form.cleaned_data['text'])
            # title, text 필드의 값이 저장이 된다.
            # post = form.save(commit=False)
            # # 현재 저장되 있는 유저네임을 가져옴
            # post.author = User.objects.get(username=request.user.username)
            # post.published_date = timezone.now()
            # # DB에 등록됌
            # post.save()
            # urls.py 에서 name='post_detail' 가져옴
            return redirect('post_detail', pk=post.pk)
    else:
        # 등록 Form 을 보여주는 부분 (get 요청)
        # forms.py 에 있는 PostForm class 를 호출해서 보여준다.
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


# Post 상세조회
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# Post 목록
def post_list(requests):
    # 이건 views 안에 Templates 를 같이 뿌려준거임
    # name = 'Django'
    # return HttpResponse('''<h2>Post List</h2>
    #     <p>웰컴 {name}!!!</p>
    #     <p>{content}</p>'''.format(name=name, content=requests.user))

    # QuerySet 을 사용하여 DB 에서 Post 목록 가져오기
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # Template 안에 선언한 HTML 를 views 에 연결 // {'posts': posts} : QuerySet
    return render(requests, 'blog/post_list.html', {'posts': posts})
