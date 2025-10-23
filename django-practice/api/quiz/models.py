from django.db import models
from ..users.models import User


class QuizHistory(models.Model):
    class Level(models.TextChoices):
        EASY = "EASY"
        NORMAL = "NORMAL"
        HARD = "HARD"

    class Amount(models.IntegerChoices):
        _5 = 5
        _10 = 10
        _20 = 20

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    level = models.TextField(choices=Level.choices)
    amount = models.IntegerField(choices=Amount.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword
