from rest_framework import serializers

from islam_fitz.survey.models import (Answer, LastPage, Question, QuestionAnswerList, Client,  ClientAnswerList)

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id','answer_title', "answer", "hasCourse", "course")

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
    answer_url = serializers.SerializerMethodField()
    class Meta:
        model = QuestionAnswerList
        fields = ('id',"question", "answer_url")
    
    def get_answer_url(self, answer):
        request = self.context.get("request")
        answer_url = answer.image.url
        return request.build_absolute_uri(answer_url)

class MyQuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswerList
        fields = ('id', "answer",)
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
            'id',
            "video",
            "description",
            "whatsapp_number"
        )


class ClientAnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAnswerList
        fields = (
            'id',
            "client",
            "client_answer",
        )
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
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
        
    



