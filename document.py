import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import SingleDocumentTranslationClient
from azure.ai.translation.document import DocumentTranslationClient
from azure.ai.translation.document.models import DocumentTranslateContent


def test():
    # create variables for your resource key, custom endpoint, sourceUrl, targetUrl, and targetLanguage
    key =  "ae73c0a952cc41fdab65d86ac21de81a"
    endpoint = "https://sunnyyuan-rg.cognitiveservices.azure.com/"
    sourceUri ="https://sunnyyuan.blob.core.windows.net/source/sample.docx?st=2024-07-21T04%3A04%3A56Z&se=2024-07-21T12%3A04%3A56Z&sp=rl&spr=https&sv=2022-11-02&sr=c&sig=c3kedBS7m5Lkfhx99TDZtLurZoQP/c3GCBB86w1blWI%3D"
    targetUri = "https://sunnyyuan.blob.core.windows.net/target/Doc1.docx?sp=w&st=2024-07-21T04:27:30Z&se=2024-07-21T12:27:30Z&sv=2022-11-02&sr=b&sig=%2FYX996N8YtXlAouA8zC1oTPM39LTpOIzkEZ4fY1ZK9Y%3D"
    targetLanguage = 'en'


    # initialize a new instance of the DocumentTranslationClient object to interact with the asynchronous Document Translation feature
    client = DocumentTranslationClient(endpoint, AzureKeyCredential(key))

    # include source and target locations and target language code for the begin translation operation
    poller = client.begin_translation(sourceUri, targetUri, targetLanguage)
    result = poller.result()

    print('Status: {}'.format(poller.status()))
    print('Created on: {}'.format(poller.details.created_on))
    print('Last updated on: {}'.format(poller.details.last_updated_on))
    print(
        'Total number of translations on documents: {}'.format(
            poller.details.documents_total_count
        )
    )

    print('\nOf total documents...')
    print('{} failed'.format(poller.details.documents_failed_count))
    print('{} succeeded'.format(poller.details.documents_succeeded_count))

    for document in result:
        print('Document ID: {}'.format(document.id))
        print('Document status: {}'.format(document.status))
        if document.status == 'Succeeded':
            print('Source document location: {}'.format(document.source_document_url))
            print(
                'Translated document location: {}'.format(document.translated_document_url)
            )
            print('Translated to language: {}\n'.format(document.translated_to))
        else:
            print(
                'Error Code: {}, Message: {}\n'.format(
                    document.error.code, document.error.message
                )
            )



def translate_document():
    # Your API key and endpoint
    key = "ae73c0a952cc41fdab65d86ac21de81a"
    endpoint = "https://sunnyyuan-rg.cognitive.microsofttranslator.com"
    
    # Initialize the DocumentTranslationClient
    client = DocumentTranslateContent(endpoint, AzureKeyCredential(key))

    # URLs for your source and target blob containers
    source_container_url = "https://sunnyyuan.blob.core.windows.net/source"
    target_container_url = "https://sunnyyuan.blob.core.windows.net/target"

    # Define the translation target with language and target URL
    translation_target = TranslationTarget(
        target_url=target_container_url,
        language_code="it"
    )

    # Begin the translation job
    job = client.begin_translation(
        source_url=source_container_url,
        targets=[translation_target]
    )

    # Wait for the translation to complete and print results
    result = job.result()
    for document in result:
        print(f"Document: {document.name}")
        print(f"Status: {document.status}")
        if document.status == "Succeeded":
            print(f"Translated document URL: {document.translated_document_url}")

def sample_single_document_translation():

    # create variables for your resource api key, document translation endpoint, and target language
    key = "ae73c0a952cc41fdab65d86ac21de81a"
    endpoint = "https://sunnyyuan-rg.cognitive.microsofttranslator.com"

    target_language = "it"

    # initialize a new instance of the SingleDocumentTranslationClient object to interact with the synchronous Document Translation feature
    client = SingleDocumentTranslationClient(endpoint, AzureKeyCredential(key))

    # absolute path to your document
    file_path = "/Users/zichenyuan/Desktop/sample.docx"
    file_name = os.path.basename(file_path)
    file_type = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    print(f"File for translation: {file_name}")

    # Open the file using the full path
    with open(file_path, "rb") as file:
        file_contents = file.read()
        # print(file_contents)

    document_content = (file_name, file_contents, file_type)
    document_translate_content = DocumentTranslateContent(document=document_content)
  
    response_stream = client.document_translate(
        body=document_translate_content, target_language=target_language
    )
    translated_response = response_stream.decode("utf-8-sig")  # type: ignore[attr-defined]
    print(f"Translated response: {translated_response}")


if __name__ == "__main__":
    # sample_single_document_translation()
    test()