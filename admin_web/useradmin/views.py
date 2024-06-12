from django.http import HttpResponseNotFound, Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users, Recruitment_course, Chats, Channels
from .serializers import UserSerializer, RecruitmentSerializer, ChatSerializer, ChannelSerializer


class Recruitment_View(APIView):

    def get(self, request, pk, format=None):
        question = Recruitment_course.objects.filter(pk__gt=pk).first()
        if not question:
            return HttpResponseNotFound()
        serialized_recruitment = RecruitmentSerializer(question, many=False)
        return Response(serialized_recruitment.data)


class UsersList(APIView):

    def get(self, request, format=None):
        queryset = Users.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetail(APIView):

    def get_object(self, user_id):
        try:
            return Users.objects.get(user_id=user_id)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, user_id, format=None):
        queryset = self.get_object(user_id)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        queryset = self.get_object(user_id)
        serializer = UserSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        queryset = self.get_object(user_id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReferalView(APIView):

    def get(self, request, referal, format=None):
        users = Users.objects.filter(referal=referal, subscription_day__isnull=False).all()
        if not users:
            return HttpResponseNotFound()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)


class ChatList(APIView):

    def get(self, request, format=None):
        queryset = Chats.objects.all()
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChannelList(APIView):

    def get(self, request, format=None):
        queryset = Channels.objects.all()
        serializer = ChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChannelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
