from django.contrib import admin

# Register your models here.

from .models import (Answer, Question, QuestionAnswerList, LastPage,
 Client, ClientAnswerList)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answer_title", "active", "hasCourse", "course")
    readonly_fields = ("answer_preview",)
    list_editable = ("active", "hasCourse", "course")

    def answer_preview(self, obj):
        return obj.answer_preview

    answer_preview.short_description = 'Answer Preview'
    answer_preview.allow_tags = True

class AnswerInline(admin.TabularInline):
    model = ClientAnswerList
    client_answer = ClientAnswerList.client_answer
    list_display = ("client_answer",)
    readonly_fields = ("client_answer",)
    max = 20
    extra = 0
    


class ClientAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display =("name", "type", "phone", "length", "weight")
    readonly_fields = ("type", "name", "phone", "length", "weight", "description")
    list_filter = ("type",)
    search_fields = ("name", "phone",)

admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question)
admin.site.register(QuestionAnswerList)
admin.site.register(Client, ClientAdmin)
# admin.site.register(ClientAnswer)
admin.site.register(ClientAnswerList)
admin.site.register(LastPage)

