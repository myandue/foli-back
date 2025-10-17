import requests

from .models import SpeechToText


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
    # Send audio file to external speech-to-text API
    api_url = "https://api.example.com/speech-to-text"

    with open(audio_file_path, "rb") as f:
        response = requests.post(api_url, files={"file": f})
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
    # Send transcription to external summarization API
    api_url = "https://api.example.com/summarize"

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


def get_quiz(transcription: str, level: int, amount: int):
    # Send transcription to external quiz generation API
    api_url = "https://api.example.com/generate-quiz"
    params = {"text": transcription, "level": level, "amount": amount}

    response = requests.post(api_url, json=params)
    response.raise_for_status()

    result = response.json()
    return result.get("quiz", [])
