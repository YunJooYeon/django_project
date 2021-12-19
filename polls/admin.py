from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# Question, Choice 한 화면에서 처리할 수 있도록 변경
# 테이블 형식으로 보기
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # 한 번에 보여주는 Choice text의 숫자

# Question 안에 항목 이름 지정 및 감추기
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # 필드 분리 및 'Date information' 접기 기능
        ('Question Statement', {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']})
    ]

    # Choice 모델 클래스 같이 보기
    inlines = [ChoiceInline]

    # 질문 목록 화면에서 보여지는 항목
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # 필터 사이드 바
    list_filter = ['pub_date']

    # 검색 바
    search_fields = ['question_text']

# Question 모델이 관리자 페이지에 등록됨
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

