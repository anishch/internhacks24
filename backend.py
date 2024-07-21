from flask import Flask, render_template, request
import os, requests, uuid, json, textract, PyPDF2

def detect_language(input):
    key= "ae73c0a952cc41fdab65d86ac21de81a"
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/translate'
    constructed_url = endpoint + path

    params= {
        'api-version':'3.0',
        'to': ['am','en']
    }
    headers= {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': 'Westus2',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body= [{
        'text': input
    }]
    # text = textract.process('pmdevspec.pdf')
    # body[0]['text'] = []
    # content = [{}]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return (response[0]["translations"])
    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print("hi")
    content = file.read().decode('utf-8')
    ### content variable is right here
    content = detect_language(content)
    print(content)
    return content

if __name__ == '__main__':
    app.run(debug=True)


