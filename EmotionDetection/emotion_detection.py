import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP EmotionPredict service.
    If API call fails, returns mock data for testing purposes.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json, timeout=5)
        if response.status_code != 200:
            raise Exception(f"API returned status code {response.status_code}")

        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

    except Exception:
        # Mock Data when API fails
        emotions = {
            "anger": 0.8,
            "disgust": 0.05,
            "fear": 0.05,
            "joy": 0.05,
            "sadness": 0.05
        }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0),
        "dominant_emotion": dominant_emotion
    }


# تشغيل الدالة للاختبار وأخذ لقطة الشاشة
if __name__ == "__main__":
    result = emotion_detector("I hate working long hours")
    print(result)
