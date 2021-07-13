from django.contrib import admin
from .models import(BeforeAndAfter, AboutUs, FAQ, Home, Footer)
# Register your models here.

admin.site.register(BeforeAndAfter)
admin.site.register(AboutUs)
admin.site.register(Home)
admin.site.register(Footer)
admin.site.register(FAQ)