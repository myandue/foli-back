import requests

from .repository import save_quiz_history


def fetch_and_save_quiz_info(user, keyword, level, amount):
    # Fetch quiz data from external API
    # api_url = "https://api.example.com/generate-quiz"
    # params = {"keyword": keyword, "level": level, "amount": amount}
    # response = requests.get(api_url, params=params)
    # response.raise_for_status()
    # quiz_data = response.json().get("results", [])

    # Mocked quiz data for demonstration purposes
    quiz_data = [
        {
            "question": (
                f"Sample question {i+1} about {keyword} at level {level}?"
            ),
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "answer": "Option A",
        }
        for i in range(amount)
    ]

    # Save quiz history
    save_quiz_history(user, keyword, level, amount)

    return quiz_data
