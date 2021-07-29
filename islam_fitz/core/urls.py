from django.urls import path, re_path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from islam_fitz.core.views import BeforeAndAfterMethod, AboutUsMethod, HomeViewMethod, FAQMethod, FooterMethod


router_core = DefaultRouter(trailing_slash=False)
router_core.register('', HomeViewMethod)
router_core.register('about', AboutUsMethod)
router_core.register('before_after', BeforeAndAfterMethod)
router_core.register('FAQ', FAQMethod)
router_core.register('footer', FooterMethod)

urlpatterns = [
    path('', include(router_core.urls)),
]