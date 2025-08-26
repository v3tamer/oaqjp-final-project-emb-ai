import requests

def emotion_detector(text_to_analyze):
    """
    دالة ترسل النص إلى خدمة واتسون لاكتشاف المشاعر
    وتعيد القيمة الموجودة في الحقل 'text' من الاستجابة
    """
    # عنوان الطلب (endpoint)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # الرؤوس
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # البيانات المرسلة
    input_json = { "raw_document": { "text": text_to_analyze } }

    # إرسال الطلب
    response = requests.post(url, headers=headers, json=input_json)

    # التحقق من الاستجابة
    if response.status_code == 200:
        # إرجاع القيمة text من الاستجابة
        return response.json().get("text", None)
    else:
        return None
