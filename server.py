"""
Flask server for the Emotion Detection application.
Serves the index page and processes emotion detection requests.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the main HTML page for the application.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Receive text input from the user, call the emotion detector,
    and return either the dominant emotion or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    # Handle blank or invalid text
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    dominant = result["dominant_emotion"]
    return f"For the given statement, the system response is {dominant}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
