from rest_framework import serializers

class InviteCodeSerializer(serializers.Serializer):
    invite_code = serializers.CharField(max_length=8)
    user_id = serializers.IntegerField()
