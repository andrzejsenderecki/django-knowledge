from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    url(r'^quiz/$', quiz_views.questions, name='quiz'),
    url(r'^quiz/result$', quiz_views.answer_result, name='result'),
]
