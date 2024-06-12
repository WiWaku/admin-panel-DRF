from rest_framework import serializers
from .models import Meeting, RecordUserMeeting
from drf_writable_nested.serializers import WritableNestedModelSerializer


class RecordUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordUserMeeting
        fields = ['user_id', 'username', 'full_name']


class MeetingSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    user = RecordUserSerializer(many=True)

    class Meta:
        model = Meeting
        fields = ['title', 'date_meeting', 'cost', 'description', 'user']
