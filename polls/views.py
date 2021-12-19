from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# 투표 목록(index) 뷰
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 6

    # 최근 생성된 질문 순으로 리턴
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

# 투표 상세(detail) 뷰
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# 투표 결과(results) 뷰
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# 투표 기능(vote) 뷰
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


class AllResultsView(generic.ListView):
    template_name = 'polls/all_results.html'
    context_object_name = 'latest_question_list'

    # 최근 생성된 질문 순으로 리턴
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')
