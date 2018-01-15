from django.db import models

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

    def __str__(self):
        return self.question_answer

class Answer2(models.Model):
    question_answer_1 = models.CharField(max_length=1)

    def __str__(self):
        return self.question_answer_1