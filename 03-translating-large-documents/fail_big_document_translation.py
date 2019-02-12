import boto3

# INPUT_DOCUMENT_NAME = 'small_document.txt'
# INPUT_DOCUMENT_NAME = 'big_document.txt'
OUTPUT_DOCUMENT_NAME = 'document_es.txt'

def translate_text(text, lang_code):
    translate = boto3.client('translate')
    result = translate.translate_text(
        Text=text,
        TerminologyNames=[
            'CloudFreeCustom',
        ],
        SourceLanguageCode='auto',
        TargetLanguageCode=lang_code
    )
    print(
        'Translated text into the language code of ' + lang_code + '.' +
        '\nSource text: "' + text + '"' + 
        '\nResult text: "' + result['TranslatedText'] + '"\n'
        )
    return result['TranslatedText']

with open(INPUT_DOCUMENT_NAME, 'r') as infile, open(OUTPUT_DOCUMENT_NAME, 'w') as outfile:
    text = infile.read()
    result = translate_text(text, 'es')
    outfile.write(result)
