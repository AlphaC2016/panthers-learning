# ICMP_redirection.py
#
# Programmer  : Guy, shaked
# Date        : 03/05/2022
#
# word api
# ------------------------------------------------------------------------------------------------------

# import
import docx
import oci
from oci.config import validate_config
from deep_translator import GoogleTranslator
import json
from googleapiclient.discovery import build
from googlesearch import search
import urllib
from bs4 import BeautifulSoup

FILENAME = r"C:\Users\kelle\Desktop\TESTW.docx"
CONFIG_FILE = r"C:\Users\kelle\.oci\config"
USER = "ocid1.user.oc1..aaaaaaaa7mxia3xroif3st7xwoglkyt3cu24h3zohcqpvpc4oo6lrpnmvuzq"
FINGERPRINT = "a7:e6:99:17:39:c9:e4:17:bb:42:f2:81:1c:d7:84:af"
TENANCY = "ocid1.tenancy.oc1..aaaaaaaa7l5viilzwmlk6gmxfyjiektpyusskdbvlwi6bzaqlvxsxy7q2ryq"
REGION = "il-jerusalem-1"
KEY_FILE = r"C:\Users\kelle\Desktop\oracel_keys\kellerg2002@gmail.com_2023-08-23T11_46_39.769Z.pem"

def read_docx():
    # Reads the docx file and returns it
    print("enter your word directory:\n")
    file = FILENAME
    doc = docx.Document(f"{file}")
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return "\n".join(fulltext)


def create_config():
    # Create a default config using DEFAULT profile in default location
    # config = oci.config.from_file(f"{CONFIG_FILE}")
    config = {
        "user": f"{USER}",
        "fingerprint": f"{FINGERPRINT}",
        "tenancy": f"{TENANCY}",
        "region": f"{REGION}",
        "key_file": f"{KEY_FILE}"
    }
    validate_config(config)
    return config

def api_ai(translated, config):
    # Get the main key phrases
    ai_language_client = oci.ai_language.AIServiceLanguageClient(config)

    batch_detect_language_key_phrases_response = ai_language_client.batch_detect_language_key_phrases(
        batch_detect_language_key_phrases_details=oci.ai_language.models.BatchDetectLanguageKeyPhrasesDetails(
            documents=[
                oci.ai_language.models.TextDocument(
                    key="doc1",
                    text=f"{translated}",
                    language_code="en")]
        ))
    print(batch_detect_language_key_phrases_response.data)
    return batch_detect_language_key_phrases_response.data

def Classify_ai(data):
    # classifys the main 5 key phrases
    data = str(data)
    json_dict = json.loads(data)
    dict5 = json_dict['documents'][0]['key_phrases'][1:5]
    print(dict5)
    return dict5

def google_search(search_term, api_key, cse_id, **kwargs):
    """this function took me soo mach time to make you
    need to create google api with google cloud and your own search engine
    welcome to PANTHERSEARCH"""

    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


def google_api_trunslet(fulltext):
    # translets the docx from hebrew to english
    to_translate = fulltext
    translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
    return translated

def google_api_trunslet_revers(translated):
    to_translate = translated
    translated = GoogleTranslator(source='en', target='iw').translate(to_translate)
    print(translated)
def main():
    my_api_key = "AIzaSyAfAAwfwQFVCKNne9WJrNixONncLSgDp38"
    my_cse_id = "3028683e43d81493a"
    fulltext = read_docx()
    translated = google_api_trunslet(fulltext)
    config = create_config()
    data = api_ai(translated, config)
    key_phrases = Classify_ai(data)

    results = google_search('"god is a woman" "thank you next" "7 rings"', my_api_key, my_cse_id, num=10)
    for result in results:
        print(result)

    #translated = google_api_trunslet_revers(translated)

if __name__ == "__main__":
    main()
