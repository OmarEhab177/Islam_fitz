from rest_framework import serializers

from islam_fitz.survey.models import (Answer, LastPage, Question, QuestionAnswerList, Client,  ClientAnswerList)

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('answer_title', "answer", "hasCourse", "course")

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            "id",
            "type",
            "question_title",
            "question",
            "hasDescription",
            "description",
            "description_title"
        )
    
class QuestionAnswerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswerList
        fields = ("question", "answer")

class MyQuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswerList
        fields = ("answer",)
        depth = 1

class QuestionAnswerSerializer(serializers.ModelSerializer):
    answer = MyQuestionAnswerSerializer(source="questionanswerlist_set", many=True)
    

    class Meta:
        model = Question
        fields = (
            "id",
            "type",
            "question_title",
            "question",
            "hasDescription",
            "description",
            "description_title",
            "answer",
        )

        depth = 1


class LastPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = LastPage
        fields = (
            "video",
            "description",
            "whatsapp_number"
        )


class ClientAnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAnswerList
        fields = (
            "client",
            "client_answer",
        )
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "type",
            "name",
            "phone",
            "length",
            "weight"
        )
        

# class ClientAnswerSerializer(serializers.ModelSerializer):
#     answer = ClientAnswerListSerializer(source="clientanswerlist_set", many=True)
#     class Meta:
#         model = Client
#         fields = (
#             "type",
#             "name",
#             "phone",
#             "length",
#             "weight",
#             "answer"
#         )
        
    



