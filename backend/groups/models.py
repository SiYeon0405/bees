from django.db import models
from users.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_groups")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default="member")

    class Meta:
        unique_together = ("group", "user")

class InviteCode(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="invite_codes")
    code = models.CharField(max_length=20, unique=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f"{self.group.name} - {self.code}"

