from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    # Get the text from the query string
    text_to_analyze = request.args.get('text')
    
    if not text_to_analyze:
        return "Please provide text to analyze", 400
    
    # Analyze the text using your function
    result = emotion_detector(text_to_analyze)
    
    # Format the response as in the example
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
