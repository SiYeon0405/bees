from django.db import models
from django.contrib.auth import get_user_model
from group_create.models import Group  # 그룹 생성 앱에서 Group 모델 가져오기

User = get_user_model()

class GroupMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'group')  # 중복 참가 방지

    def __str__(self):
        return f"{self.user.username} joined {self.group.name}"
