from django.db import models
from django.utils import timezone
from django import forms

# Model 은 class 정의한 후 "python manage.py makemigrations blog" 로 데이터베이스 migrations

# Modelform 추가
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('제목은 3글자 이상 입력해 주세요!')


class Post(models.Model):
    # 작성자
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # ForeignKey 는 class
    # 제목
    title = models.CharField(max_length=200, validators=[min_length_3_validator])
    # 내용
    text = models.TextField()
    # 작성일자
    created_date = models.DateTimeField(default=timezone.now)
    # 게시일자
    published_date = models.DateTimeField(blank=True, null=True)
    # 필드 추가 - 삭제할 예정
    # test = models.TextField()

    # 게시일자에 현재날짜시간을 대입해주는 함수
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 객체주소 대신 글제목을 반환해주는 함수 : JAVA 에선 toString() 함수
    def __str__(self):
        return self.title

    # 승인된 Comments 만 반환해주는 함수
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


# Post 에 달리는 댓글 Comment 클래스
class Comment(models.Model):
    # post 에 id를 저장 / post 정보
    # related_name='comments' >> 여러 정보에 댓글이 달릴 수 있도록 하니까 comments 라고 이름 지정
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    # 댓글 작성자
    author = models.CharField(max_length=100)
    # 댓글 내용
    text = models.TextField()
    # 댓글 작성일자
    created_date = models.DateTimeField(default=timezone.now)
    # BooleanField >> 댓글 승인 여부
    approved_comment = models.BooleanField(default=False)

    # 댓글 승인하기
    # 클래스 안에 method 형식처럼 만들어서 필요할때마다 함수 호출하기 위함.
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
