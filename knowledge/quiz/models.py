from django.db import models
from django.conf import settings

class Question(models.Model):
    question_number = models.CharField(max_length=100)
    question_text = models.TextField()
    answer_a = models.CharField(max_length=400)
    answer_b = models.CharField(max_length=400)
    answer_c = models.CharField(max_length=400)
    answer_d = models.CharField(max_length=400)
    answer_good = models.CharField(max_length=1)

    def __str__(self):
        return self.question_number

class Answer1(models.Model):
    question_answer = models.CharField(max_length=1)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.question_answer

class Answer2(models.Model):
    question_answer_1 = models.CharField(max_length=1)
    student_2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.question_answer_1

class Answer3(models.Model):
    question_answer_2 = models.CharField(max_length=1)
    student_3 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.question_answer_2

class Answer4(models.Model):
    question_answer_3 = models.CharField(max_length=1)
    student_4 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.question_answer_3

class Answer5(models.Model):
    question_answer_4 = models.CharField(max_length=1)
    student_5 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.question_answer_4

class Answer6(models.Model):
    question_answer_5 = models.CharField(max_length=1)
    student_6 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.question_answer_5
