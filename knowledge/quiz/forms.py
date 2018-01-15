from django import forms
from .models import Answer1, Answer2, Question

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer1
        fields = ('question_answer',)

class AnswerForm1(forms.ModelForm):
    class Meta:
        model = Answer2
        fields = ('question_answer_1',)


