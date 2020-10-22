from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):  # ModelAdmin class 상속받아서 재구성
    # list_display 는 ModelAdmin 의 속성 (게시글 화면에 보이게 설정)
    list_display = ['id', 'title', 'count_text']
    # 'title' 에 링크를 주겠다.
    list_display_links = ['title']

    def count_text(self, obj):
        return '{}글자'.format(len(obj.text))
    # short_description >> 설정을 안해주면 'count_text' 함수 이름 그대로 나옴
    count_text.short_description = 'text 글자수'


# Post 계정을 보이게 하려면 밑에 추가, PostAdmin 우리가 따로 만들어서 커스텀 마이징 한거임
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
