from transformers import pipeline


classifier = pipeline(
    "sentiment-analysis",
    model="wonrax/phobert-base-vietnamese-sentiment"
)

label_map = {
    "POS": "positive",
    "NEG": "negative",
    "NEU": "neutral"
}

def analyze_sentiment(comment, rating=None):
    """
    Phân tích cảm xúc từ comment
    Trả về: positive / negative / neutral
    """

    if not comment or comment.strip() == "":
        return "neutral"

    try:
        result = classifier([comment])[0]
        label = result['label']

        sentiment = label_map.get(label, "neutral")

        return sentiment

    except Exception as e:
        print("Sentiment error:", e)
        return "neutral"
