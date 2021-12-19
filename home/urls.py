from django.urls import path
from .import views

app_name = 'home'

urlpatterns = [
    # url이 'home/'으로 끝났을 때 HomeView 호출
    path('', views.HomeView.as_view(), name='home'),
]