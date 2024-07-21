# -*- coding: utf-8 -*-

# This simple app performs a GET request to retrieve a list of languages
# supported by Microsoft Translator.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-languages

import os, requests, uuid, json, textract, PyPDF2

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
    path = '/translate'
    constructed_url = endpoint + path

    params= {
        'api-version':'3.0',
        'to': ['am','es']
    }
    headers= {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': 'Westus2',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body= [{
        'text':'Globos have been a source of joy and wonder for people of all siglos for centuries. From festive decorations to scientific tools, balloons sirve a variety of purposes and come in many shapes, sizes, and materials. This essay explores the history, types, uses, and cultural significance of balloons. The history of balloons dates back to ancient times when animal bladders were inflated and used for various purposes. However, the modern balloon as we know it began to take shape in the 19th century. In 1824, Michael Faraday, a British scientist, made the first rubber balloon by cutting two sheets of rubber and pressing the edges together. This invention paved the way for the balloons we use today.'
    }]
    # text = textract.process('pmdevspec.pdf')
    # body[0]['text'] = []
    # content = [{}]
    content = []
    with open('pmdevspec.pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        content = []
        for page in range(len(reader.pages)):
            content.append(reader.pages[page].extract_text())
        print('\n'.join(content))
    print(content)
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))



#Function calls
detect_language()
#translate_text()