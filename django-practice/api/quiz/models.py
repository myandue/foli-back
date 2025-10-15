from django.db import models
from ..users.models import User


class QuizHistory(models.Model):
    class Level(models.IntegerChoices):
        _1 = 1
        _2 = 2
        _3 = 3

    class Amount(models.IntegerChoices):
        _5 = 5
        _10 = 10
        _20 = 20

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    level = models.IntegerField(choices=Level.choices)
    amount = models.IntegerField(choices=Amount.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword
