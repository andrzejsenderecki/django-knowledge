from django.shortcuts import render
from .models import Question

def question_list(request):
    questions_all = Question.objects.all()
    context = {'questions_all': questions_all}
    return render(request, 'quiz/question_list.html', context)
