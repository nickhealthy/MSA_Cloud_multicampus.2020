from django import forms
from .models import Post, Comment


# Validator 함수 정의
# title 입력필드의 길이 체크 < 3
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('Title은 3글자 이상 입력해 주세요!')


# PostForm 클래스 선언
# <> model class 는 Model 를 상속받음
class PostForm(forms.Form):
    # validators=[min_length_3_validator] 강제에러
    title = forms.CharField(validators=[min_length_3_validator])
    # title = forms.CharField()
    # input 대신 >> 입력할게 많으니까 Textarea
    text = forms.CharField(widget=forms.Textarea)


# ModelForm 을 상속 받는 PostModelForm 클래스 선언
class PostModelForm(forms.ModelForm):
    # 모델폼은 규칙이 이렇게 됌
    class Meta:
        model = Post
        # tuple 형식이라 뒤에 콤마
        fields = ('title', 'text',)


# ModelForm 을 상속받는 CommentModelForm 클래스 선언
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', )
