import pandas as pd
from textblob import TextBlob
from flask import Flask, jsonify, request

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

app = Flask(__name__)


def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    return snt


@app.route("/sentiment/v1")
def find_sentiment():
    query = request.args.get("query")
    blob = TextBlob(query)
    compount2 = blob.sentiment.polarity
    result = print_sentiment_scores(query)

    if (compount2 >= 0.1):
        sentiment_2 = "positive"
    elif (compount2 >= -0.1) and (compount2 < 0.1):
        sentiment_2 = "neutral"
    else:
        sentiment_2 = "negative"

    if (result["compound"] >= 0.2):
        sentiment_1 = "positive"
    elif (result["compound"] >= 0) and (result["compound"] < 0.2):
        sentiment_1 = "neutral"
    else:
        sentiment_1 = "negative"

    print("First model ==> "+sentiment_1, result["compound"])
    print("Second model ==> "+sentiment_2, compount2)
    print("\n*************************************************")
    return jsonify({
        "model_1_score": result["compound"],
        "model_1_display": sentiment_1,
        "model_2_score": compount2,
        "model_2_display": sentiment_2,
    })
