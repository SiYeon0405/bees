<<<<<<< HEAD
# users/urls.py
=======
>>>>>>> b8481a2 (feat: 회원가입 기능 복구 및 정상 작동 확인)
from django.urls import path
from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view()),
<<<<<<< HEAD
]
=======
]
>>>>>>> b8481a2 (feat: 회원가입 기능 복구 및 정상 작동 확인)
