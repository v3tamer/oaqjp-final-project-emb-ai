"""
Flask web application for emotion detection.
Provides an endpoint to analyze text and return emotion scores.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Analyze the text from the query string using emotion_detector.
    Returns a formatted string with emotion scores or an error message.
    """
    # Get the text from the query string
    text_to_analyze = request.args.get('text', '')

    # Analyze the text
    result = emotion_detector(text_to_analyze)

    # Error handling for empty or invalid text
    if result['dominant_emotion'] is None:
        return "نص غير صالح! يرجى المحاولة مرة أخرى!", 400

    # Format the response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
