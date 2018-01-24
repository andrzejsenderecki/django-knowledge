from django.shortcuts import render
from django.http import Http404
from .models import Question, Answer1, Answer2, Answer3
from .forms import AnswerForm, AnswerForm1, AnswerForm2
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.conf import settings

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

    return render(request, 'quiz/quiz.html', {'question_single': question_single, 'question_single_2': question_single_2, 'question_single_3': question_single_3, 'answer_form': answer_form, 'answer_form_1': answer_form_1, 'answer_form_2': answer_form_2})

@login_required
def answer_result(request):
    final_result = 0
    final_result_text = 'none'

    ans1_user = User.objects.get(username=request.user)
    ans1_answer = Answer1.objects.get(student=ans1_user)
    ans1 = str(ans1_answer)
    question_single = Question.objects.get(pk=1)
    ans_good = str(question_single.answer_good)

    if ans1 == ans_good:
        good_bad_1 = 'Good Answer!'
        final_result += 1
    else:
        good_bad_1 = 'Bad Answer!'

    ans2_user = User.objects.get(username=request.user)
    ans2_answer = Answer2.objects.get(student_2=ans2_user)
    ans2 = str(ans2_answer)
    question_single_2 = Question.objects.get(pk=2)
    ans_good_2 = str(question_single_2.answer_good)

    if ans2 == ans_good_2:
        good_bad_2 = 'Good Answer!'
        final_result += 1
    else:
        good_bad_2 = 'Bad Answer!'

    ans3_user = User.objects.get(username=request.user)
    ans3_answer = Answer3.objects.get(student_3=ans3_user)
    ans3 = str(ans3_answer)
    question_single_3 = Question.objects.get(pk=3)
    ans_good_3 = str(question_single_3.answer_good)

    if ans3 == ans_good_3:
        good_bad_3 = 'Good Answer!'
        final_result += 1
    else:
        good_bad_3 = 'Bad Answer!'

    if final_result < 2:
        final_result_text = 'You did not answer good on 50% questions. You Lost!'
    elif final_result > 1:
        final_result_text = 'You did answer good at least on 50% questions. You Win!'

    return render(request, 'quiz/result.html', {'question_single': question_single, 'good_bad_1': good_bad_1, 'question_single_2': question_single_2, 'good_bad_2': good_bad_2, 'question_single_3': question_single_3, 'good_bad_3': good_bad_3, 'final_result': final_result, 'final_result_text': final_result_text,})