from django.contrib import admin

# Register your models here.

from .models import (Answer, Question, QuestionAnswerList, LastPage,
 Client, ClientAnswerList)

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(QuestionAnswerList)
admin.site.register(Client)
# admin.site.register(ClientAnswer)
admin.site.register(ClientAnswerList)
admin.site.register(LastPage)
