from django.shortcuts import render
from django.http import HttpResponse

#Client로부터 request를 받아서 HttoResponse로 return하는게 기본
#그 사이에 부가적인 기능이 들어갈 수도
def index(request):
    return HttpResponse("Hello, world.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)