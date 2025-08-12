
# summarizer.py
def get_summary(text, word_limit=50):
    words = text.split()
    return ' '.join(words[:word_limit]) + '...'