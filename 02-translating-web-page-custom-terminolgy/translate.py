# pip3 install beautifulsoup4 boto3 requests

import boto3
import urllib
from bs4 import BeautifulSoup

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
    return result['TranslatedText']

def created_translated_webpage(html, to_lang_code):
    soup = BeautifulSoup(html, 'html.parser')
    for element in soup.find_all(string=lambda x: x.strip()):
        new_text = translate_text(str(element), to_lang_code)
        element.replaceWith(new_text)
    output_file = './website/index_' + to_lang_code + '.html'
    with open(output_file, "w") as file:
        file.write(str(soup))

with urllib.request.urlopen('http://globotranslatetest1123.s3-website-us-east-1.amazonaws.com/') as f:
    page_html = f.read().decode('utf-8')

for i in ['pt', 'es', 'de']:
    created_translated_webpage(page_html, i)
