from rest_framework import serializers
from .models import SpeechToText


class SpeechToTextSerializer(serializers.ModelSerializer):
    audio_file = serializers.FileField(required=True)

    class Meta:
        model = SpeechToText
        fields = [
            "id",
            "user",
            "audio_file",
            "transcription",
            "summary",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "transcription",
            "summary",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "audio_file": {"required": True},
        }

    def validate_audio_file(self, value):
        if not value.name.lower().endswith((".wav", ".mp3", ".m4a")):
            raise serializers.ValidationError("Unsupported file type.")
        if value.size > 10 * 1024 * 1024:  # 10MB limit
            raise serializers.ValidationError(
                "File size exceeds the limit of 10MB."
            )
        return value
