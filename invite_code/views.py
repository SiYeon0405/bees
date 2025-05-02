from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from group_create.models import Group
from group_join.models import GroupMembership
from django.contrib.auth import get_user_model

User = get_user_model()

class InviteJoinView(APIView):
    def post(self, request):
        code = request.data.get("invite_code")
        user_id = request.data.get("user_id")

        try:
            group = Group.objects.get(invite_code=code)
            user = User.objects.get(id=user_id)
        except Group.DoesNotExist:
            return Response({"error": "유효하지 않은 초대코드입니다."}, status=400)
        except User.DoesNotExist:
            return Response({"error": "사용자가 존재하지 않습니다."}, status=400)

        if GroupMembership.objects.filter(user=user, group=group).exists():
            return Response({"message": "이미 가입한 그룹입니다."}, status=200)

        GroupMembership.objects.create(user=user, group=group)
        return Response({"message": "그룹에 참가했습니다."}, status=201)
