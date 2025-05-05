from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from .models import User

class SignupView(APIView):
    renderer_classes = [JSONRenderer]  # JSON 응답

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
