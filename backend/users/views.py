from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import update_session_auth_hash

from .models import User
from .serializers import (
    EmailTokenObtainPairSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
    PasswordChangeSerializer
)

# ✅ 회원가입 뷰
class SignupView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [AllowAny]  # 인증 없이 접근 가능

    def get(self, request):
        return Response({'error': 'GET 요청은 지원되지 않습니다.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        nickname = request.data.get('nickname')

        if not email or not password or not nickname:
            return Response({'error': '모든 항목을 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': '이미 존재하는 이메일입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(nickname=nickname).exists():
            return Response({'error': '이미 존재하는 닉네임입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        User.objects.create_user(email=email, password=password, nickname=nickname)
        return Response({'message': '회원가입이 완료되었습니다.'}, status=status.HTTP_201_CREATED)


# ✅ 이메일 기반 JWT 로그인 뷰
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


# ✅ 마이페이지: 사용자 정보 조회 및 수정
class MyPageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '정보가 수정되었습니다.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):  # ✅ PATCH 메서드 추가
        serializer = UserUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '정보가 수정되었습니다.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 비밀번호 변경
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            if not request.user.check_password(serializer.validated_data['old_password']):
                return Response({'error': '기존 비밀번호가 틀렸습니다.'}, status=status.HTTP_400_BAD_REQUEST)

            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            update_session_auth_hash(request, request.user)  # 세션 갱신 유지
            return Response({'message': '비밀번호가 변경되었습니다.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ 회원 탈퇴
class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        request.user.delete()
        return Response({'message': '계정이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
