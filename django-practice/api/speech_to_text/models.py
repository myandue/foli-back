from django.db import models
from ..users.models import User


class SpeechToText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(
        upload_to="uploads/audio/", null=False, blank=True
    )
    transcription = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transcription by {self.user.username} at {self.created_at}"
