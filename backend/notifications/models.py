from django.db import models
from django.conf import settings  # 커스텀 유저 모델 참조용

class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # 커스텀 유저 모델 참조
        on_delete=models.CASCADE
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간 자동 저장

    def __str__(self):
        return f'{self.user.email}: {self.message[:20]}...'
