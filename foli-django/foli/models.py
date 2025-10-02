from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class RefreshToken(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active"
        REVOKED = "revoked"
        EXPIRED = "expired"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    user_agent = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_on = models.DateTimeField()

    def __str__(self):
        return f"RefreshToken for {self.user.username}"


class QuizHistory(models.Model):
    class Level(models.TextChoices):
        1
        2
        3

    class Amount(models.TextChoices):
        5
        10
        20

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    level = models.CharField(max_length=1, choices=Level.choices)
    amount = models.CharField(max_length=2, choices=Amount.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SpeechToText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_url = models.URLField()
    transcription = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transcription by {self.user.username} at {self.created_at}"
