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
import requests
import json

#Keren 11111
FILENAME = r"C:\Users\kelle\Desktop\TESTW.docx"
PRIVATE_KEY = r"C:\Users\kelle\Desktop\oracel_keys\kellerg2002@gmail.com_2023-08-23T11_46_39.769Z.pem"
def read_docx():
    # Reads the docx file and returns it
    print("enter your word directory:\n")
    file = FILENAME
    doc = docx.Document(f"{file}")
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return "\n".join(fulltext)

# def api_trunslet(translated):
#     # Text Translation
#
#     # Create a default config using DEFAULT profile in default location
#     # config = oci.config.from_file(r"C:\Users\kelle\.oci\config")
#     config = {
#         "user" : "ocid1.user.oc1..aaaaaaaa7mxia3xroif3st7xwoglkyt3cu24h3zohcqpvpc4oo6lrpnmvuzq",
#     "fingerprint" : "a7:e6:99:17:39:c9:e4:17:bb:42:f2:81:1c:d7:84:af",
#     "tenancy" : "ocid1.tenancy.oc1..aaaaaaaa7l5viilzwmlk6gmxfyjiektpyusskdbvlwi6bzaqlvxsxy7q2ryq",
#     "region" : "il-jerusalem-1",
#     "key_file" : r"C:\Users\kelle\Desktop\oracel_keys\kellerg2002@gmail.com_2023-08-23T11_46_39.769Z.pem"
#     }
#     validate_config(config)
#     # Initialize service client with default config file
#     ai_language_client = oci.ai_language.AIServiceLanguageClient(config)
#
#     batch_detect_language_key_phrases_response = ai_language_client.batch_detect_language_key_phrases(
#         batch_detect_language_key_phrases_details=oci.ai_language.models.BatchDetectLanguageKeyPhrasesDetails(
#             documents=[
#                 oci.ai_language.models.TextDocument(
#                     key="doc1",
#                     text=f"{translated}",
#                     language_code="en")]
#         ))
#
#     # Get the data from response
#     print(batch_detect_language_key_phrases_response.data)
def api_ai(translated):
    # Text Translation

    # Create a default config using DEFAULT profile in default location
    # config = oci.config.from_file(r"C:\Users\kelle\.oci\config")
    config = {
        "user": "ocid1.user.oc1..aaaaaaaa7mxia3xroif3st7xwoglkyt3cu24h3zohcqpvpc4oo6lrpnmvuzq",
        "fingerprint": "a7:e6:99:17:39:c9:e4:17:bb:42:f2:81:1c:d7:84:af",
        "tenancy": "ocid1.tenancy.oc1..aaaaaaaa7l5viilzwmlk6gmxfyjiektpyusskdbvlwi6bzaqlvxsxy7q2ryq",
        "region": "il-jerusalem-1",
        "key_file": f"{PRIVATE_KEY}"
    }
    validate_config(config)
    # Initialize service client with default config file
    ai_language_client = oci.ai_language.AIServiceLanguageClient(config)

    batch_detect_language_key_phrases_response = ai_language_client.batch_detect_language_key_phrases(
        batch_detect_language_key_phrases_details=oci.ai_language.models.BatchDetectLanguageKeyPhrasesDetails(
            documents=[
                oci.ai_language.models.TextDocument(
                    key="doc1",
                    text=f"{translated}",
                    language_code="en")]
        ))

    # Get the data from response
    print(batch_detect_language_key_phrases_response.data)


    #URL = "https://language.il-jerusalem-1/20210101/actions/batchDetectLanguageKeyPhrases"
    #response = requests.get(URL)
    #print(response)
    #print()
   # json_response = json.loads(response.text)
   # print(json_response)
  #  data = response.json({
   #   "documents": [
   #     {
   #       "key": "doc1",
  #        "text": f"{translated}"
   #     }
  #    ]
  #  })


def google_api_trunslet(fulltext):
    """translets the docx from hebrew to english"""
    to_translate = fulltext
    translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
    print(translated)
    return translated

def google_api_trunslet_revers(translated):
    to_translate = translated
    translated = GoogleTranslator(source='en', target='iw').translate(to_translate)
    print(translated)
def main():

    fulltext = read_docx()
    print(fulltext)
    translated = google_api_trunslet(fulltext)
    api_ai(translated)
    translated = google_api_trunslet_revers(translated)

if __name__ == "__main__":
    main()
