from textblob import TextBlob

NEGATIVE_WORDS = [
    "tệ", "tệ hại", "xấu", "dở",
    "khó chịu", "chán", "bực", "kinh khủng", "thất vọng", "đáng ghét", "khủng khiếp", "tồi", "dở ẹc","không tốt"
]

POSITIVE_WORDS = [
    "hay", "tốt", "tuyệt vời", "xuất sắc", "đỉnh", "tuyệt", "đẹp", "thú vị", "vui", "hài lòng", "tuyệt vời", "hoàn hảo", "xuất sắc","ổn"
]

from textblob import TextBlob

def analyze_sentiment(text, rating):
    text = text.lower()

    # 1. Phân tích nội dung
    if any(w in text for w in NEGATIVE_WORDS):
        text_sentiment = "negative"
    elif any(w in text for w in POSITIVE_WORDS):
        text_sentiment = "positive"
    else:
        text_sentiment = "neutral"

    # 2. Phân tích sao
    if rating <= 2:
        star_sentiment = "negative"
    elif rating == 3:
        star_sentiment = "neutral"
    else:
        star_sentiment = "positive"

    # 3. KẾT HỢP
    if text_sentiment == star_sentiment:
        return text_sentiment

    # Nếu mâu thuẫn → trung lập
    return "neutral"

