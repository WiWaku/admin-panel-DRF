from .models import Users, Recruitment_course, Chats, Channels
from rest_framework import serializers


class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment_course
        fields = ['flag']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'user_name', 'testing_attempts', 'user_lvl', 'subscription_day', 'access_quiz',
                  'subscription_name', 'email_google', 'referal', 'referal_sub']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ['title', 'tg_id']


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channels
        fields = ['title', 'tg_id']

#
# class StatisticsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Statistics
#         fields = ['new_user', 'purchase_month', 'purchase_three_month', 'purchase_meeting', 'passed_test', 'failed_test']
