from django.db import models
from django.urls import reverse

# Create your models here.

# Bookmark에서 사용할 Bookmark 테이블
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # 객체를 출력할 때 나타낼 값 : admin 사이트 Bookmark 목록에 나타낼 이름
    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # 북마크 수정 후 detail 화면으로 돌아감
    def get_absolute_url(self):
        return reverse('bookmark:detail', args=[str(self.id)])