from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Competition


class ListCompetitionsView(APIView):
    def get(self, request):
        competitions = Competition.objects.values("market")
        print(competitions)
        return Response({"count": 0})
