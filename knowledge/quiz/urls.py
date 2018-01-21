from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^quiz/$', quiz_views.question_single, name='quiz'),
    url(r'^quiz/result$', quiz_views.answer_result, name='answer_result'),
]
