from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class GroupJoinViewSet(ViewSet):
    def create(self, request):
        return Response({'message': '그룹 참가 테스트 성공'})
