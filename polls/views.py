from django.shortcuts import get_object_or_404, render
from django.http import Http404

from django.http import HttpResponse
from django.template import loader
from .models import Question

#Client로부터 request를 받아서 HttoResponse로 return하는게 기본
#그 사이에 부가적인 기능이 들어갈 수도
def index(request):
    #1
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    #context = {
        #"latest_question_list": latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
    
    #2
    #render를 쓰면 줄일 수 도 있음
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    #1
    #return HttpResponse("You're looking at question %s." % question_id)
    
    #2
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, "polls/detail.html", {"question": question})
    
    #3
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)