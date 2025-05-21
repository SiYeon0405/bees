from rest_framework import serializers
from .models import GroupMembership

class GroupJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembership
        fields = '__all__'
        read_only_fields = ['joined_at']