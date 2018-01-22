from django.shortcuts import render
from django.http import Http404
from .models import Question, Answer1, Answer2, Answer3
from .forms import AnswerForm, AnswerForm1, AnswerForm2
from django.contrib.auth.decorators import login_required

@login_required
def question_single(request):

    try:
        question_single = Question.objects.get(pk=1)
    except Question.DoesNotExist:
        raise Http404("Not found question!")

    try:
        question_single_2 = Question.objects.get(pk=2)
    except Question.DoesNotExist:
        raise Http404("Not found question")

    try:
        question_single_3 = Question.objects.get(pk=3)
    except Question.DoesNotExist:
        raise Http404("Not found question")

    answer_form = AnswerForm(data=request.POST)

    if request.method == 'POST':
        if answer_form.is_valid():
            new_answer = answer_form.save(commit=False)
            new_answer.student = request.user
            new_answer.save()
        else:
            answer_form = AnswerForm()

    answer_form_1 = AnswerForm1(data=request.POST)
    if request.method == 'POST':
        if answer_form_1.is_valid():
            new_answer_1 = answer_form_1.save(commit=False)
            new_answer_1.student_2 = request.user
            new_answer_1.save()
        else:
            answer_form_1 = AnswerForm1()

    answer_form_2 = AnswerForm2(data=request.POST)
    if request.method == 'POST':
        if answer_form_2.is_valid():
            new_answer_2 = answer_form_2.save(commit=False)
            new_answer_2.student_3 = request.user
            new_answer_2.save()
        else:
            answer_form_1 = AnswerForm1()

    return render(request, 'quiz/single.html', {'question_single': question_single, 'question_single_2': question_single_2, 'question_single_3': question_single_3, 'answer_form': answer_form, 'answer_form_1': answer_form_1, 'answer_form_2': answer_form_2})

@login_required
def answer_result(request):
    final_result = 0
    final_result_text = 'none'
    try:
        question_single = Question.objects.get(pk=1)
    except Question.DoesNotExist:
        raise Http404("Not found question!")

    try:
        question_single_2 = Question.objects.get(pk=2)
    except Question.DoesNotExist:
        raise Http404("Not found question")

    try:
        question_single_3 = Question.objects.get(pk=3)
    except Question.DoesNotExist:
        raise Http404("Not found question")

    try:
        answer_1 = Answer1.objects.get()
        answer_question_1 = Question.objects.get(pk=1)
        if answer_1.question_answer == answer_question_1.answer_good:
            good_bad_1 = 'Good Answer!'
            final_result += 1
        else:
            good_bad_1 = 'Bad Answer!'
    except Question.DoesNotExist:
        raise Http404("Not found question!")

    try:
        answer_2 = Answer2.objects.get()
        answer_question_2 = Question.objects.get(pk=2)
        if answer_2.question_answer_1 == answer_question_2.answer_good:
            good_bad_2 = 'Good Answer!'
            final_result += 1
        else:
            good_bad_2 = 'Bad Answer!'
    except Question.DoesNotExist:
        raise Http404("Not found question!")

    try:
        answer_3 = Answer3.objects.get()
        answer_question_3 = Question.objects.get(pk=3)
        if answer_3.question_answer_2 == answer_question_3.answer_good:
            good_bad_3 = 'Good Answer!'
            final_result += 1
        else:
            good_bad_3 = 'Bad Answer!'
    except Question.DoesNotExist:
        raise Http404("Not found question!")

    if final_result < 2:
        final_result_text = 'You did not answer good on 50% questions. You Lost!'
    elif final_result > 1:
        final_result_text = 'You did answer good at least on 50% questions. You Win!'

    return render(request, 'quiz/score.html', {'answer_1': answer_1, 'good_bad_1': good_bad_1, 'answer_2': answer_2, 'good_bad_2': good_bad_2, 'answer_3': answer_3, 'good_bad_3': good_bad_3, 'answer_result': answer_result, 'final_result_text': final_result_text, 'question_single': question_single, 'question_single_2': question_single_2, 'question_single_3': question_single_3,})