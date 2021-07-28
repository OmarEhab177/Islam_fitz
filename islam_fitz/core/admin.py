from django.contrib import admin
from .models import(BeforeAndAfter, AboutUs, FAQ, Home, Footer)
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = "Islam Fitz"
admin.site.site_title = "Fitz"

admin.site.register(BeforeAndAfter)
admin.site.register(AboutUs)
admin.site.register(Home)
admin.site.register(Footer)
admin.site.register(FAQ)
admin.site.unregister(Group)
admin.site.unregister(Site)

