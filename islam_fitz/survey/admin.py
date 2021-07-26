from django.contrib import admin

# Register your models here.

from .models import (Answer, Question, QuestionAnswerList, LastPage,
 Client, ClientAnswerList)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "answer_title", "active", "hasCourse", "course")
    readonly_fields = ("answer_preview",)

    def answer_preview(self, obj):
        return obj.answer_preview

    answer_preview.short_description = 'Answer Preview'
    answer_preview.allow_tags = True

# class AnswerInline(admin.TabularInline):
#     model = ClientAnswerList
#     # answer_image = ClientAnswerList.client_answer
#     # list_display = ("answer_image",)


# class ClientAdmin(admin.InlineModelAdmin):
#     model = Client
#     inlines = ["AnswerInline",]

admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question)
admin.site.register(QuestionAnswerList)
admin.site.register(Client)
# admin.site.register(ClientAnswer)
admin.site.register(ClientAnswerList)
admin.site.register(LastPage)

