from islam_fitz.core.models import BeforeAndAfter, AboutUs, FAQ, Home, Footer
from islam_fitz.core.serializers import BeforeAndAfterSerializer, AboutUsSerializer, FAQSerializer, HomeSerializer, FooterSerializer
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
    if "feature" passed in paramater it will retrieve last 8 'before and after' objects 
    "/v1/api/before_after?feature"
    """

    permission_classes = [AllowAny]
    queryset = BeforeAndAfter.objects.none()

    def list(self, request):
        bAf = BeforeAndAfter.objects.all()
        feature = request.GET.get("feature")
        if (feature is not None):
            bAf = bAf.filter(feature=True)
            bAf = bAf.distinct()
            bAf = bAf[::-1][:8]
        else:
            bAf = bAf[::-1]
        ser = BeforeAndAfterSerializer(bAf, many=True)
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
        ser = AboutUsSerializer(about, many=True)
        return Response(ser.data, status=200)


class HomeMethod(viewsets.ViewSet):
    """
    Retrieve:
    retrieve Home page
    """

    permission_classes = [AllowAny]
    queryset = Home.objects.none()

    def list(self, request):
        home = Home.objects.all()
        ser = HomeSerializer(home, many=True)
        return Response(ser.data, status=200)

class FooterMethod(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = Footer.objects.none()

    def list(self, request):
        footer = Footer.objects.all()
        ser = FooterSerializer(footer, many=True)
        return Response(ser.data, status=200)

class FAQMetod(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = Footer.objects.none()

    def list(self, request):
        faq = FAQ.objects.all()
        ser = FAQSerializer(faq, many=True)
        return Response(ser.data, status=200)
