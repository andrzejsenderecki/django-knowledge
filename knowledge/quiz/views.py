from django.shortcuts import render
from django.http import Http404
from .models import Question, Answer1, Answer2
from .forms import AnswerForm, AnswerForm1

def question_single(request, question_id):
    try:
        question_single = Question.objects.get(pk=1)
    except Question.DoesNotExist:
        raise Http404("Not found question!")

    try:
        question_single_2 = Question.objects.get(pk=2)
    except Question.DoesNotExist:
        raise Http404("Not found question")

    answer_form = AnswerForm(data=request.POST)
    if request.method == 'POST':
        if answer_form.is_valid():
            new_answer = answer_form.save()
            new_answer.save()
        else:
            answer_form = AnswerForm()

    answer_form_1 = AnswerForm1(data=request.POST)
    if request.method == 'POST':
        if answer_form_1.is_valid():
            new_answer_1 = answer_form_1.save()
            new_answer_1.save()
        else:
            answer_form_1 = AnswerForm1()

    return render(request, 'quiz/single.html', {'question_single': question_single, 'question_single_2': question_single_2, 'answer_form': answer_form, 'answer_form_1': answer_form_1})
