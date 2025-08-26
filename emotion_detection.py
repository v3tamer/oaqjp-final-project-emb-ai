import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP EmotionPredict service,
    extracts the required emotions with their scores,
    determines the dominant emotion, and returns results in a dictionary.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        if response.status_code != 200:
            return None

        # Parse JSON response string into Python dictionary
        formatted_response = json.loads(response.text)

        # Extract emotion scores
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        anger_score = emotions.get("anger", 0)
        disgust_score = emotions.get("disgust", 0)
        fear_score = emotions.get("fear", 0)
        joy_score = emotions.get("joy", 0)
        sadness_score = emotions.get("sadness", 0)

        # Determine dominant emotion
        emotion_scores = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return in required format
        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }

    except Exception as e:
        return {"error": str(e)}
