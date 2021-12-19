from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    # url이 'login/'로 끝났을 때 LoginView 호출
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),

    # url이 'logout/'로 끝났을 때 LogoutView 호출
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # url이 'signup/'로 끝났을 때 signup 호출
    path('signup/', views.signup, name='signup'),
]