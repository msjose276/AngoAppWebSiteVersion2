from django.contrib import admin
from .models import Person
from .models import Partner
from .models import Photo
from .models import Project

# Register your models here.


class PartnerAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name','link']

class PersonAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name','email','role','administrator','bio','linkedin','github','facebook']

class PhotoInline(admin.TabularInline):
    model = Photo

# Project admin class featuring the Color model and model actions
class ProjectAdmin(admin.ModelAdmin):
    ordering = ['-publishedDate']
    list_display = ['title', 'client','publishedDate']
    inlines = [PhotoInline]


admin.site.register(Partner, PartnerAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Project, ProjectAdmin)

