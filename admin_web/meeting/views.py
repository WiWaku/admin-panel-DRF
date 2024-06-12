from django.http import HttpResponseNotFound, Http404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Meeting, RecordUserMeeting
from .serializers import MeetingSerializer
from rest_framework import status


class MeetingView(APIView):

    def get(self, request, format=None):
        users = Meeting.objects.all()
        if not users:
            return HttpResponseNotFound()
        serialized_users = MeetingSerializer(users, many=True)
        return Response(serialized_users.data)


class MeetingDetail(APIView):

    def get_object(self, title):
        try:
            return Meeting.objects.get(title=title)
        except Meeting.DoesNotExist:
            raise Http404

    def get(self, request, title, format=None):
        queryset = self.get_object(title)
        serializer = MeetingSerializer(queryset, read_only=True)
        return Response(serializer.data)


@api_view(["POST"])
def Append_user(request: Request):
    RecordUserMeeting(
        meeting_id = request.data["pk"],
        user_id=request.data["user_id"],
        username=request.data["username"],
        full_name = request.data['full_name']
    ).save()
    return Response(data={"status": "SUCCESS"})

