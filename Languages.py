# -*- coding: utf-8 -*-

# This simple app performs a GET request to retrieve a list of languages
# supported by Microsoft Translator.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-languages

import os, requests, uuid, json

#Instance Variables


#Function to translate text to different languages
def translate_text():
    key= "ae73c0a952cc41fdab65d86ac21de81a"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/languages?api-version=3.0'
    constructed_url = endpoint + path 

    headers = {
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    request = requests.get(constructed_url, headers=headers)
    response = request.json()

    print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))

#Function that detects and translates text
def detect_language():
    key= "ae73c0a952cc41fdab65d86ac21de81a"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/languages?api-version=3.0'
    constructed_url = endpoint + path

    params= {
        'api-version':'3.0',
        'to': ['am','en']
    }
    headers= {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': 'westus',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body= [{
        'text':'Hola como esta!'
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))



#Function calls
detect_language()
#translate_text()