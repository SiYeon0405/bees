from django.urls import path
from .views import (
    SignupView,
    EmailTokenObtainPairView,
    MyPageView,
    ChangePasswordView,
    DeleteAccountView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),  # ✅ 회원가입
    path('login/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),  # ✅ JWT 로그인 (이메일 기반)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ✅ 토큰 갱신

    path('mypage/', MyPageView.as_view(), name='mypage'),  # ✅ 사용자 정보 조회 & 수정
    path('password/', ChangePasswordView.as_view(), name='change_password'),  # ✅ 비밀번호 변경
    path('delete/', DeleteAccountView.as_view(), name='delete_account'),  # ✅ 회원 탈퇴
]
