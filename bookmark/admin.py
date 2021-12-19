from django.contrib import admin
from .models import Bookmark  # models.py 파일에 정의한 Bookmark 클래스를 가져옴

# Register your models here.
admin.site.register(Bookmark)