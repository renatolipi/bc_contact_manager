from django.contrib import admin

from .models import Person, LastContactTalk


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', )
    search_fields = ['name', ]


class LastContactTalkAdmin(admin.ModelAdmin):
    list_display = ('last_contact_date', 'person', )
    list_filter = ('person__name', )
    search_fields = ['person__name', ]

admin.site.register(Person, PersonAdmin)
admin.site.register(LastContactTalk, LastContactTalkAdmin)
