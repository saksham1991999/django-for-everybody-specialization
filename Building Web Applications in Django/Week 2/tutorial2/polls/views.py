
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse




from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

# Create your views here.
def owner(request):
    return HttpResponse("Hello, world. a6e8ad49 is the polls index.")

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)