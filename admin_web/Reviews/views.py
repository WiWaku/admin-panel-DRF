from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reviews_model
from .serializers import RevSerializer


class Reviews_View(APIView):
    def get(self, request, pk, format=None):
        question = Reviews_model.objects.filter(pk__gt=pk).first()
        if not question:
            return HttpResponseNotFound()
        serialized_recruitment = RevSerializer(question, many=False)
        return Response(serialized_recruitment.data)
