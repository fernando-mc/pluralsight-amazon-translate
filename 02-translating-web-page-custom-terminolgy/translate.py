import boto3
import urllib
from bs4 import BeautifulSoup

WEBSITE_URL = "REPLACE_WITH_URL"
TERMINOLOGY_NAME = "REPLACE_WITH_NAME"

def translate_text(text, lang_code):
    translate = boto3.client('translate')
    result = translate.translate_text(
        Text=text,
        TerminologyNames=[
            TERMINOLOGY_NAME,
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

def created_translated_webpage(html, to_lang_code):
    soup = BeautifulSoup(html, 'html.parser')
    for element in soup.find_all(string=lambda x: x.strip()):
        new_text = translate_text(str(element), to_lang_code)
        element.replaceWith(new_text)
    output_file = './website/index_' + to_lang_code + '.html'
    with open(output_file, "w") as file:
        file.write(str(soup))
    print('Finished translating HTML into the language code of: ' + to_lang_code + '\n\n')

with urllib.request.urlopen(WEBSITE_URL) as f:
    page_html = f.read().decode('utf-8')

for i in ['pt', 'es', 'de']:
    created_translated_webpage(page_html, i)
