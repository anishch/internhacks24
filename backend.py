from flask import Flask, render_template, request
import os, requests, uuid, json, textract, PyPDF2

from openai import OpenAI

totalDocument = ""

client = OpenAI(
    # This is the default and can be omitted
    api_key="sk-proj-DO8NOFbyodvp8KAENMulT3BlbkFJoLQQD4InpA8ixXMtsARz"
)

def detect_language(input):
    global totalDocument;
    totalDocument = input
    print(totalDocument)
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
    print(response)
    print(response[0]["translations"])
    return (response[0]["translations"])
    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/respond', methods=['POST'])
def respond():
    print("we're here")
    member_variable = request.data.decode('utf-8')
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a profession legal assistant with knowledge of the following document. Document: \"" 
             + totalDocument + "\". Answer the user's questions as precisely as you can, and if something they ask is not within the scope of the prompt, tell them that is not in the document."},
            {"role": "user", "content": member_variable}
        ]
    )
    # print(response.choices[0].message.content)
    output = response.choices[0].message.content    
    # print(output)
    return output

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print("hi")
    content = file.read().decode('utf-8')
    ### content variable is right here
    content = detect_language(content)
    totalDocument = content
    # print(content)
    return content

if __name__ == '__main__':
    app.run(debug=True)


