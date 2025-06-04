from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


# ✅ 이메일 기반 JWT 로그인 시리얼라이저
class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            email=email,
            password=password
        )

        if user is None:
            raise serializers.ValidationError("유효하지 않은 이메일 또는 비밀번호입니다.")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


# ✅ 마이페이지용 사용자 정보 조회 시리얼라이저
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "nickname",
            "profile_image",
            "introduction",
            "date_joined"
        ]
        read_only_fields = ["id", "email", "date_joined"]


# ✅ 사용자 정보 수정용 시리얼라이저
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname", "profile_image", "introduction"]


# ✅ 비밀번호 변경 시리얼라이저
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


# 25.06.04 추가 -홍
class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD  # 일반적으로 'email'

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )
            if not user:
                raise serializers.ValidationError('이메일 또는 비밀번호가 올바르지 않습니다.', code='authorization')
        else:
            raise serializers.ValidationError('이메일과 비밀번호를 모두 입력해주세요.', code='authorization')

        refresh = self.get_token(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
            }
        }