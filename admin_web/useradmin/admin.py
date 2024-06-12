from django.contrib import admin
from .models import Users, Recruitment_course, Chats, Channels


class UsersAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name']


admin.site.register(Users, UsersAdmin)


@admin.register(Recruitment_course)
class RecruitmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Chats)
class ChatsAdmin(admin.ModelAdmin):
    pass


@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
    pass


# @admin.register(Statistics)
# class StatisticsAdmin(admin.ModelAdmin):
#     pass
