from rest_framework import serializers

from islam_fitz.core.models import BeforeAndAfter, AboutUs, FAQ, Home, Footer

class BeforeAndAfterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BeforeAndAfter
        fields = (
            "id",
            "name",
            "description",
            "image",
            "feature",
            "active",
        )

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            "photo",
            "description"
        )

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = (
            "logo",
            "intro_image",
            "intro_text",
            "about_us_image",
            "about_us_text"

        )

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model: Footer
        fields = (
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
            "question",
            "answer"
        )