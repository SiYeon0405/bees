from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny  # ✅ 추가
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainPairSerializer
from .models import User


# ✅ 회원가입 뷰
class SignupView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [AllowAny]  # ✅ 인증 없이 접근 가능

    def get(self, request):
        return Response({'error': 'GET 요청은 지원되지 않습니다.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        nickname = request.data.get('nickname')  # ✅ 프론트에서도 nickname 보내도록 해야 함

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
