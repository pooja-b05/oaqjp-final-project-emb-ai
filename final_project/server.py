from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")

    # Call emotion detection function
    response = emotion_detector(text_to_analyze)

    # Handle empty or invalid response
    if response is None or "dominant_emotion" not in response:
        return "Invalid text! Please try again."

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format response as required
    result_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)