from django.urls import path, re_path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from islam_fitz.survey.views import (ClientAnswerMethod, CreateClientAnswerMethod, QuestionAnswerMethod, LastPageMethod,
 AnotherQuestionAnswerMethod, NewCreateClientAnswerMethod)

router = DefaultRouter(trailing_slash=False)
router.register('questions', QuestionAnswerMethod)
router.register('another_questions', AnotherQuestionAnswerMethod)
router.register('last_page', LastPageMethod)
router.register('client/answer', ClientAnswerMethod)
router.register('client/answer/create', NewCreateClientAnswerMethod)
router.register('client/answer/add', CreateClientAnswerMethod)


# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls))
]
