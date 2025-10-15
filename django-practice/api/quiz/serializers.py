from rest_framework import serializers
from .models import QuizHistory


class QuizHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizHistory
        fields = "__all__"
        read_only_fields = ("user", "created_at", "updated_at")
