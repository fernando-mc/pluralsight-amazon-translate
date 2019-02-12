import boto3

INPUT_DOCUMENT_NAME = 'big_document.txt'

def translate_text(text, lang_code):
    translate = boto3.client('translate')
    result = translate.translate_text(
        Text=text,
        SourceLanguageCode='auto',
        TargetLanguageCode=lang_code
    )
    print(
        'Translated text into the language code of ' + lang_code + '.' +
        '\nSource text: "' + text + '"' + 
        '\nResult text: "' + result['TranslatedText'] + '"\n'
        )
    return result['TranslatedText']

def translate_large_document(input_filename, output_filename, lang_code):
    # Placeholder for parts of translated document 
    final_document_array = []
    # Read the initial document text
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        text = infile.read()
        # Split it up by paragraph and clean up unused spaces
        text_array = text.split('\n')
        clean_text_array = list(filter(lambda x: x != '', text_array))
        # Translate the paragraphs
        for i in clean_text_array:
            final_document_array.append(translate_text(i, lang_code))
            final_document_array.append('\n\n')
        # Write the translated paragraphs to a new file
        for paragraph in final_document_array:
            outfile.write(paragraph)

translate_large_document(INPUT_DOCUMENT_NAME, 'big_document_es.txt', 'es')
