
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from group_create.models import Group
from group_join.models import GroupMembership
from django.contrib.auth import get_user_model

import random
import string


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


User = get_user_model()

class InviteCreateView(APIView):
    """
    POST /api/invite/
    body: {"group_id": <int>}
    → 그룹에 8자리 랜덤 초대코드를 생성·저장하고 반환
    """
    def post(self, request):
        group_id = request.data.get("group_id")
        if not group_id:
            return Response(
                {"error": "group_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response(
                {"error": "존재하지 않는 그룹입니다."},
                status=status.HTTP_404_NOT_FOUND
            )

        # 8자리 영문+숫자 코드 생성
        code = "".join(random.choices(string.ascii_letters + string.digits, k=8))

        # Group.invite_code에 저장
        group.invite_code = code
        group.save(update_fields=["invite_code"])

        return Response(
            {"code": code, "group_id": group_id},
            status=status.HTTP_201_CREATED
        )


