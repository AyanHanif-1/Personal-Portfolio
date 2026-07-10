from django.contrib import admin

from .models import Contact , Projects , Skills

# Register your models here.

admin.site.register(Contact)
admin.site.register(Projects)
admin.site.register(Skills)

admin.site.site_header = "Ayan's Portfolio Admin"
admin.site.site_title = "Portfolio Dashboard"
admin.site.index_title = "Welcome to the Portfolio Management Panel"