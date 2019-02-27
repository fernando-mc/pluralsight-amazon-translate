import boto3
import time

INPUT_DOCUMENT_NAME = 'big_document.txt'
OUTPUT_DOCUMENT_NAME = 'document_es.txt'


def fail_translation():
    translate = boto3.client('translate')
    with open(INPUT_DOCUMENT_NAME, 'r') as infile:
        try:
            result = translate.translate_text(
                Text=infile.read(),
                SourceLanguageCode='auto',
                TargetLanguageCode='es'
            )
            print(result['TranslatedText'])
        except:
            print('Translation failed')


i = 0
while i < 100:
    fail_translation()
    time.sleep(2)
