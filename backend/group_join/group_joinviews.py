from rest_framework import viewsets
from .models import GroupMembership
from .serializers import GroupJoinSerializer

class GroupJoinViewSet(viewsets.ModelViewSet):
    queryset = GroupMembership.objects.all()
    serializer_class = GroupJoinSerializer
