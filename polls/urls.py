from django.urls import path
from . import views

app_name = 'polls'

# 제너릭 뷰
urlpatterns = [
    # ex: /polls/
    # polls  다음이 '공백'이면 인덱스 뷰가 동작하고 이름을 인덱스로 부여
    path('', views.IndexView.as_view(), name='index'),

    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /polls/allresults
    path('polls/allresults/', views.AllResultsView.as_view(), name='allresults'),

]
