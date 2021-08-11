from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

# Create your models here.

################################## Sending data ##############################

class Answer(models.Model):
    answer_title = models.CharField(max_length=255)
    answer    = models.ImageField(upload_to = 'photos/answers/%y/%m/%d')
    active    = models.BooleanField(default=True)
    hasCourse = models.BooleanField(default=False)
    course    = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answer'

    @property
    def answer_preview(self):
        if self.answer:
            _answer = get_thumbnail(self.answer,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_answer.url, _answer.width, _answer.height))
        return ""

    def __str__(self):
        return self.answer_title



class Question(models.Model):
    TYPE_CHOICES = [
        ("Man", "Man"),
        ("Woman", "Woman")
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    question_title = models.CharField(max_length=255)
    question = models.CharField(max_length=400)
    active = models.BooleanField(default=True)
    hasDescription = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    description_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class QuestionAnswerList(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer   = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta(object):
        unique_together = [
            ("question", "answer"),
        ]
        verbose_name = "QuestionAnswerList"
        verbose_name_plural = "QuestionAnswerList"

    def __str__(self):
        return self.question.question


class LastPage(models.Model):
    video = models.FileField(upload_to="videos/%y/%m/%d")
    description = models.TextField()
    whatsapp_text = models.CharField(max_length=250, default="تواصل واتساب لبدء المتابعه")
    whatsapp_number = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'LastPage'
        verbose_name_plural = 'LastPage'

##############################################################################



################################# Received Data #############################

# class ClientAnswer(models.Model):
#     # client_answer = models.ImageField(upload_to = 'photos/client_answers/%y/%m/%d')
#     client_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


#     class Meta:
#         verbose_name = 'ClientAnswer'
#         verbose_name_plural = 'ClientAnswer'

class Client(models.Model):
    type   = models.CharField(max_length=15)
    name   = models.CharField(max_length=255)
    phone  = models.CharField(max_length=50, unique=True)
    length = models.CharField(max_length=15)
    weight = models.CharField(max_length=15)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    def __str__(self):
        return self.name
    
class ClientAnswerList(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    client_answer = models.ForeignKey(Answer ,on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'ClientAnswerList'
        verbose_name_plural = 'ClientAnswerList'

    def __str__(self):
        return self.client.name

##############################################################################

