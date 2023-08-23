import textdescriptives as td
from deep_translator import GoogleTranslator
import urllib.request
from bs4 import BeautifulSoup

def get_data(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    # print(text[:4000])
    return text[:4000]

def google_api_trunslet(fulltext):
    """translets the docx from hebrew to english"""
    to_translate = fulltext
    translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
    return translated

def google_api_trunslet_revers(translated):
    to_translate = translated
    translated = GoogleTranslator(source='en', target='iw').translate(to_translate)
    return translated

def analyze(text):
    # will automatically download the relevant model (´en_core_web_lg´) and extract all metrics
    df = td.extract_metrics(text=text, lang="en", metrics=None)

    # specify spaCy model and which metrics to extract
    df = td.extract_metrics(text=text, spacy_model="en_core_web_lg", metrics=["readability", "coherence"])
    return df["coleman_liau_index"] * 0.4 + df["lix"] * 0.4 + df["flesch_reading_ease"]*0.2


def Infer(url):
    text = get_data(url)
    translated = google_api_trunslet(text)
    return analyze(translated)
