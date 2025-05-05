from django.db import models
from groups.models import Group

class File(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="files")
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class FileVersion(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name="versions")
    version_number = models.IntegerField()
    uploaded_file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

