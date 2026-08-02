from analyzer import analyze_message
from services.url_analyzer import analyze_url


def process_message(message):
    return analyze_message(message)


def process_url(url):
    return analyze_url(url)