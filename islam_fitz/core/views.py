from django.db.models.query import EmptyQuerySet
from islam_fitz.core.models import BeforeAndAfter, AboutUs, FAQ, Home, Footer
from islam_fitz.core.serializers import BeforeAndAfterSerializer, AboutUsSerializer, FAQSerializer, HomeSerializer, FooterSerializer, PaginatorBeforeAndAfterSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

class BeforeAndAfterMethod(viewsets.ViewSet):
    """
    list:
    return before and after images:
    take the following paramater:
    - feature
    - page     int  add number of page u want to access
    if "feature" passed in paramater it will retrieve number of feature 'before and after' objects 
    "/v1/api/before_after?feature"
    """

    permission_classes = [AllowAny]
    queryset = BeforeAndAfter.objects.none()

    def list(self, request):
        bAf = BeforeAndAfter.objects.all()
        page = request.GET.get('page')
        feature = request.GET.get("feature")
        if (feature is not None and feature !=""):
            feature = int(feature)
            bAf = bAf.filter(feature=True)
            bAf = bAf.distinct()
            bAf = bAf[::-1][:feature]
        else:
            bAf = bAf[::-1]
        ser = PaginatorBeforeAndAfterSerializer(bAf, request, 12)
        return Response(ser.data, status=200)

class AboutUsMethod(viewsets.ViewSet):
    """
    Retrieve:
    retrieve aboutUs page
    """
    permission_classes = [AllowAny]
    queryset = AboutUs.objects.none()

    def list(self, request):
        about = AboutUs.objects.all()
        ser = AboutUsSerializer(about, context={"request": request}, many=True)
        return Response(ser.data, status=200)


class HomeViewMethod(viewsets.ViewSet):
    """
    Retrieve:
    retrieve Home page
    """

    permission_classes = [AllowAny]
    queryset = Home.objects.none()

    def list(self, request):
        home = Home.objects.all()
        ser = HomeSerializer(home, context={"request": request}, many=True)
        return Response(ser.data, status=200)

class FooterMethod(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = Footer.objects.none()

    def list(self, request):
        footer = Footer.objects.all()
        ser = FooterSerializer(footer, many=True)
        return Response(ser.data, status=200)

class FAQMethod(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = Footer.objects.none()

    def list(self, request):
        faq = FAQ.objects.all()
        ser = FAQSerializer(faq, many=True)
        return Response(ser.data, status=200)
