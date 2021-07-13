from django.urls import path, re_path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from islam_fitz.survey.views import (ClientAnswerMethod, CreateClientAnswerMethod, QuestionAnswerMethod, LastPageMethod)

router = DefaultRouter(trailing_slash=False)
router.register('survey', QuestionAnswerMethod)
router.register('last_page', LastPageMethod)
router.register('client/answer', ClientAnswerMethod)
router.register('client/answer/create', CreateClientAnswerMethod)


# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls))
]
