from django import forms
from .models import Answer1, Answer2, Answer3, Answer4, Answer5, Answer6, Question

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer1
        fields = ('question_answer',)
        labels = {
            "question_answer": "Answer: a, b, c or d"
        }

class AnswerForm1(forms.ModelForm):
    class Meta:
        model = Answer2
        fields = ('question_answer_1',)
        labels = {
            "question_answer_1": "Answer: a, b, c or d"
        }

class AnswerForm2(forms.ModelForm):
    class Meta:
        model = Answer3
        fields = ('question_answer_2',)
        labels = {
            "question_answer_2": "Answer: a, b, c or d"
        }

class AnswerForm3(forms.ModelForm):
    class Meta:
        model = Answer4
        fields = ('question_answer_3',)
        labels = {
            "question_answer_3": "Answer: a, b, c or d"
        }

class AnswerForm4(forms.ModelForm):
    class Meta:
        model = Answer5
        fields = ('question_answer_4',)
        labels = {
            "question_answer_4": "Answer: a, b, c or d"
        }

class AnswerForm5(forms.ModelForm):
    class Meta:
        model = Answer6
        fields = ('question_answer_5',)
        labels = {
            "question_answer_5": "Answer: a, b, c or d"
        }