import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# Question 테이블
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): # 데이터베이스에 대한 객체를 출력해줄 때
        return self.question_text # question_text로 출력

    def was_published_recently(self): # 최근 등록 여부 구분
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 질문 목록 화면에서 보여지는 was_published_recently 아이콘으로 보이기
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# Choice 테이블
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
