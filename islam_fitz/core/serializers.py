from django.http import request
from rest_framework import serializers

from islam_fitz.core.models import BeforeAndAfter, AboutUs, FAQ, Home, Footer
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class PaginatorBeforeAndAfterSerializer():
    def __init__(self, beforeAndAfter, request, num):
        paginator = Paginator(beforeAndAfter, num)
        page = request.query_params.get('page')
        try:
           beforeAndAfter =  paginator.page(page)
        except PageNotAnInteger:
            beforeAndAfter = paginator.page(1)
        except EmptyPage:
            beforeAndAfter = paginator.page(paginator.num_pages)
        count = paginator.count
        previous = None if not beforeAndAfter.has_previous() else beforeAndAfter.previous_page_number()
        next = None if not beforeAndAfter.has_next() else beforeAndAfter.next_page_number()
        serializer = BeforeAndAfterSerializer(beforeAndAfter, context={"request": request}, many=True)
        self.data = {'count':count,'previous':previous,
                 'next':next,'BeforeAndAfter':serializer.data}

class BeforeAndAfterSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = BeforeAndAfter
        fields = (
            "id",
            "name",
            "description",
            "image_url",
            "feature",
            "active",
        )
    def get_image_url(self, beforeAndAfter):
        request = self.context.get("request")
        image_url = beforeAndAfter.image.url
        return request.build_absolute_uri(image_url)

class AboutUsSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    class Meta:
        model = AboutUs
        fields = (
            "id",
            "photo_url",
            "description"
        )
    def get_photo_url(self, aboutUs):
        request = self.context.get("request")
        photo_url = aboutUs.photo.url
        return request.build_absolute_uri(photo_url)

class HomeSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    intro_image_url = serializers.SerializerMethodField()
    about_us_image_url = serializers.SerializerMethodField()
    text_image_url = serializers.SerializerMethodField()
    class Meta:
        model = Home
        fields = (
            "id",
            "logo_url",
            "text_image_url",
            "first_text",
            "intro_title",
            "intro_image_url",
            "intro_text",
            "about_us_image_url",
            "about_us_text",
        )
    def get_logo_url(self, home):
        request = self.context.get("request")
        logo_url = home.logo.url
        return request.build_absolute_uri(logo_url)
    
    def get_intro_image_url(self, home):
        request = self.context.get("request")
        intro_image_url = home.intro_image.url
        return request.build_absolute_uri(intro_image_url)
    
    def get_about_us_image_url(self, home):
        request = self.context.get("request")
        about_us_image_url = home.about_us_image.url
        return request.build_absolute_uri(about_us_image_url)

    def get_text_image_url(self, home):
        request = self.context.get("request")
        text_image_url = home.text_image.url
        return request.build_absolute_uri(text_image_url)

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = (
            "id",
            "facebook",
            "instagram",
            "youtube",
            "address",
            "email",
            "first_phone_number",
            "second_phone_number"
        )
    
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = (
            "id",
            "question",
            "answer"
        )