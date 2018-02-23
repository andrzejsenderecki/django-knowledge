from django.shortcuts import render
from django.http import Http404
from .models import Question, Answer1, Answer2, Answer3, Answer4, Answer5, Answer6
from .forms import AnswerForm, AnswerForm1, AnswerForm2, AnswerForm3, AnswerForm4, AnswerForm5
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def questions(request):
    try:
        is_user = User.objects.get(username=request.user)
        is_answer = Answer1.objects.get(student=is_user)
    except:
        is_answer = 0

    if is_answer == 0:
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
            question_single_4 = Question.objects.get(pk=4)
        except Question.DoesNotExist:
            raise Http404("Not found question")

        try:
            question_single_5 = Question.objects.get(pk=5)
        except Question.DoesNotExist:
            raise Http404("Not found question")

        try:
            question_single_6 = Question.objects.get(pk=6)
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
                answer_form_2 = AnswerForm2()

        answer_form_3 = AnswerForm3(data=request.POST)
        if request.method == 'POST':
            if answer_form_3.is_valid():
                new_answer_3 = answer_form_3.save(commit=False)
                new_answer_3.student_4 = request.user
                new_answer_3.save()
            else:
                answer_form_3 = AnswerForm3()

        answer_form_4 = AnswerForm4(data=request.POST)
        if request.method == 'POST':
            if answer_form_4.is_valid():
                new_answer_4 = answer_form_4.save(commit=False)
                new_answer_4.student_5 = request.user
                new_answer_4.save()
            else:
                answer_form_4 = AnswerForm4()

        answer_form_5 = AnswerForm5(data=request.POST)
        if request.method == 'POST':
            if answer_form_5.is_valid():
                new_answer_5 = answer_form_5.save(commit=False)
                new_answer_5.student_6 = request.user
                new_answer_5.save()
            else:
                answer_form_5 = AnswerForm5()

        return render(request, 'quiz/quiz.html', {'question_single': question_single,
                                                  'question_single_2': question_single_2,
                                                  'question_single_3': question_single_3,
                                                  'question_single_4': question_single_4,
                                                  'question_single_5': question_single_5,
                                                  'question_single_6': question_single_6,
                                                  'answer_form': answer_form,
                                                  'answer_form_1': answer_form_1,
                                                  'answer_form_2': answer_form_2,
                                                  'answer_form_3': answer_form_3,
                                                  'answer_form_4': answer_form_4,
                                                  'answer_form_5': answer_form_5,})
    else:
        return render(request, 'quiz/answered.html')


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

    ans4_user = User.objects.get(username=request.user)
    ans4_answer = Answer4.objects.get(student_4=ans4_user)
    ans4 = str(ans4_answer)
    question_single_4 = Question.objects.get(pk=4)
    ans_good_4 = str(question_single_4.answer_good)

    if ans4 == ans_good_4:
        good_bad_4 = 'Good Answer!'
        final_result += 1
    else:
        good_bad_4 = 'Bad Answer!'

    ans5_user = User.objects.get(username=request.user)
    ans5_answer = Answer5.objects.get(student_5=ans5_user)
    ans5 = str(ans5_answer)
    question_single_5 = Question.objects.get(pk=5)
    ans_good_5 = str(question_single_5.answer_good)

    if ans5 == ans_good_5:
        good_bad_5 = 'Good Answer!'
        final_result += 1
    else:
        good_bad_5 = 'Bad Answer!'

    ans6_user = User.objects.get(username=request.user)
    ans6_answer = Answer6.objects.get(student_6=ans6_user)
    ans6 = str(ans6_answer)
    question_single_6 = Question.objects.get(pk=6)
    ans_good_6 = str(question_single_6.answer_good)

    if ans6 == ans_good_6:
        good_bad_6 = 'Good Answer!'
        final_result += 1
    else:
        good_bad_6 = 'Bad Answer!'

    if final_result < 2:
        final_result_text = 'You did not answer good on 50% questions. You Lost!'
    elif final_result > 1:
        final_result_text = 'You did answer good at least on 50% questions. You Win!'

    return render(request, 'quiz/result.html', {'question_single': question_single, 'good_bad_1': good_bad_1,
                                                'question_single_2': question_single_2, 'good_bad_2': good_bad_2,
                                                'question_single_3': question_single_3, 'good_bad_3': good_bad_3,
                                                'question_single_4': question_single_4, 'good_bad_4': good_bad_4,
                                                'question_single_5': question_single_5, 'good_bad_5': good_bad_5,
                                                'question_single_6': question_single_6, 'good_bad_6': good_bad_6,
                                                'final_result': final_result,
                                                'final_result_text': final_result_text,})