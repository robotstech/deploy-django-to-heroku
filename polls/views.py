from decouple import config
from django.shortcuts import render, HttpResponse


# Create your views here.
from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all()

    context = {
        "questions": questions
    }

    return render(request, "polls/index.html", context)


def environment(request):
    return HttpResponse(config('ENVIRONMENT'))
