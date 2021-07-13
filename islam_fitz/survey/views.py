from islam_fitz.survey.models import (Answer, Question, QuestionAnswerList, Client, ClientAnswerList, LastPage)
from .serializers import (AnswerSerializer, ClientAnswerListSerializer,ClientSerializer, QuestionSerializer, QuestionAnswerListSerializer,
 QuestionAnswerSerializer, MyQuestionAnswerSerializer, LastPageSerializer)
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser



class QuestionAnswerMethod(viewsets.ViewSet):
    """
    list:
    Return questions and answers.
    takes the following fields:
    - type  "Man or Woman"
    """

    permission_classes = [AllowAny]
    queryset = Question.objects.none()

    def list(self, request):
        data = JSONParser().parse(request)
        sex_type = data['type']
        question = Question.objects.all()
        questions = question_type_filter(question, sex_type)
        print("questions: ", questions)
        print("len questions: ", len(questions))
        if len(questions) == 0:
            return Response("Invalid data!", status=400)
        ser = QuestionAnswerSerializer(questions, many=True)
        return Response(ser.data)
        



def question_type_filter(question, sex_type):
    '''
    method to filter question survey to retrieve active question and filter it about type
    '''
    active_question = Question.objects.filter(active=True)
    question_type = active_question.filter(type=sex_type)
    questions = []
    for i in question_type:
        if i.id not in questions:
            questions.append(i.id)
    for j in question:
        if j.id not in questions:
            question = question.exclude(id=j.id)
    return (question)
    

class LastPageMethod(viewsets.ViewSet):
    """
    retrieve:
    return last page object
    """

    permission_classes = [AllowAny]
    queryset = LastPage.objects.none()

    def list(self, request):
        lastpage = LastPage.objects.all()
        ser = LastPageSerializer(lastpage, many=True)
        return Response(ser.data, status=200)


class ClientAnswerMethod(viewsets.ViewSet):
    """
    create:
    Return client answers list
    takes the following fields:
    """

    permission_classes = [AllowAny]
    queryset = Question.objects.none()

    def list(self, request):
        client = Client.objects.all()
        print("clients: ", client)
        print("len clients: ", len(client))
        if len(client) == 0:
            return Response("Invalid data!", status=400)
        ser = ClientSerializer(client, many=True)
        return Response(ser.data)


class CreateClientAnswerMethod(viewsets.ViewSet):
    """
    create:
    Create client answers list, takes the following parameters:
    - type
    - name
    - phone
    - length
    - weight
    - answer
    """
    permission_classes = [AllowAny]
    queryset = Question.objects.none()
    
    def create(self, request):
        data = JSONParser().parse(request)
        answer = data['answer']
        client_data = {"type":data["type"], "name":data["name"], "phone":data["phone"], "length":data["length"], "weight":data["weight"]}
        client_ser = ClientSerializer(data=client_data)
        if client_ser.is_valid():
            client_ser.save()
            print("client_ser.data",client_ser.data)
            print("answer",answer)
            answersID=[]
            for i in range(len(answer)):
                x = answer[i]['client_answer']
                answersID.append(x)
                i = i+1
            print("answerID: ", answersID)
            clientID = Client.objects.get(phone=data["phone"]).id
            i = 0
            for j in answersID:
                clientAnswer_data = {"client":clientID, "client_answer":answersID[i]}
                clientAnswer_ser = ClientAnswerListSerializer(data = clientAnswer_data)
                i = i+1
                if clientAnswer_ser.is_valid():
                    clientAnswer_ser.save()
                else:
                    return Response("Invaliddd data!", status=400)
            return Response("Client created successfully", status=201)
        return Response("Invalid data!", status=400)



