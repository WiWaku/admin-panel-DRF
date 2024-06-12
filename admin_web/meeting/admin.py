from django.contrib import admin
from .models import Meeting, RecordUserMeeting


class RecordAdmin(admin.TabularInline):
    model = RecordUserMeeting


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):

    list_display = ['title', 'date_meeting', 'cost', 'description']
    inlines = [RecordAdmin]
