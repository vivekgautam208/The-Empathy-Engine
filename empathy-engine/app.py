from flask import Flask, render_template, request, url_for
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

# create audio folder
os.makedirs("static/audio", exist_ok=True)

analyzer = SentimentIntensityAnalyzer()


def detect_emotion(text):

    score = analyzer.polarity_scores(text)

    if score['compound'] >= 0.05:
        return "positive"

    elif score['compound'] <= -0.05:
        return "negative"

    else:
        return "neutral"


def generate_voice(text, emotion):

    # unique filename to avoid cache
    file_id = str(uuid.uuid4())

    filename = f"{file_id}.mp3"

    filepath = f"static/audio/{filename}"

    # emotion based speed
    if emotion == "negative":
        slow = True
    else:
        slow = False

    tts = gTTS(text=text, lang="en", slow=slow)

    tts.save(filepath)

    return filename


@app.route("/", methods=["GET", "POST"])
def index():

    audio_file = None
    emotion = None

    if request.method == "POST":

        text = request.form["text"]

        emotion = detect_emotion(text)

        audio_file = generate_voice(text, emotion)

    return render_template("index.html", audio_file=audio_file, emotion=emotion)


if __name__ == "__main__":
    app.run(debug=True)