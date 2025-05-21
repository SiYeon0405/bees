from rest_framework import serializers
from .models import Group

'''
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'created_at']
'''

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'description', 'created_at']  # ✅ description 추가
