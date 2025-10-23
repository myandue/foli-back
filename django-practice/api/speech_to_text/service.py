import requests
import os

from .models import SpeechToText

AI_SERVER_URL = os.getenv("AI_SERVER_URL", "http://localhost:9000")


def process_audio_transcription(speech_to_text_id: int):
    try:
        speech_to_text_instance = SpeechToText.objects.get(
            id=speech_to_text_id
        )
    except SpeechToText.DoesNotExist:
        return ValueError("The instance not found.")

    transcription = fetch_speech_to_text_and_save(
        speech_to_text_instance.audio_file.path
    )

    speech_to_text_instance.transcription = transcription
    speech_to_text_instance.save()

    return transcription


def fetch_speech_to_text_and_save(audio_file_path: str):
    api_url = f"{AI_SERVER_URL}/api/stt/transcription"

    with open(audio_file_path, "rb") as f:
        response = requests.post(api_url, files={"audio_file": f})
        response.raise_for_status()

    result = response.json()
    return result.get("transcription", "")


def process_audio_summary(speech_to_text_id: int):
    try:
        speech_to_text_instance = SpeechToText.objects.get(
            id=speech_to_text_id
        )
    except SpeechToText.DoesNotExist:
        return ValueError("The instance not found.")

    summary = fetch_summary_and_save(speech_to_text_instance.transcription)

    speech_to_text_instance.summary = summary
    speech_to_text_instance.save()

    return summary


def fetch_summary_and_save(transcription: str):
    api_url = f"{AI_SERVER_URL}/api/documents/summary"

    response = requests.post(api_url, json={"text": transcription})
    response.raise_for_status()

    result = response.json()
    return result.get("summary", "")


def process_audio_quiz(speech_to_text_id: int, level: int, amount: int):
    try:
        speech_to_text_instance = SpeechToText.objects.get(
            id=speech_to_text_id
        )
    except SpeechToText.DoesNotExist:
        return ValueError("The instance not found.")

    quiz = get_quiz(speech_to_text_instance.transcription, level, amount)

    return quiz


def get_quiz(transcription: str, level: str, amount: int):
    api_url = f"{AI_SERVER_URL}/api/quiz/documents"
    params = {"docs": transcription, "level": level, "amount": amount}

    response = requests.post(api_url, json=params)
    response.raise_for_status()

    return response.json().get("questions", [])
