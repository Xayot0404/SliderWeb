from django.contrib import admin
from .models import *


admin.site.register(Web_Design)
admin.site.register(WebDesignModel2)
# admin.site.register(WebDesignModel3)
# admin.site.register(WebDesignModel4)
# admin.site.register(WebDesignModel5)
# admin.site.register(WebDesignModel6)
# admin.site.register(Presentation)


class WebDesignModel1Admin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at')


class WebDesignModel2Admin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at')

class WebDesignModel3Admin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at')

class WebDesignModel4Admin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at')

class WebDesignModel5Admin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at')
    
class WebDesignModel6Admin(admin.ModelAdmin):
    list_display = ('name', 'title', 'created_at')

class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'ppt_file', 'html_file')