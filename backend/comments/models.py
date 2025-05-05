from django.db import models
from groups.models import Group
from users.models import User

class Comment(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

