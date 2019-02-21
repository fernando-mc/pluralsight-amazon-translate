import boto3
import random
import time


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


text_segments = [
    "Hello!",
    "This is Plrualsight!",
    "What's your name?",
    "Nice to meet you!",
    "Congratulations!",
    "Happy birthday!",
    "During the opposition of 1894 a great light was seen on the illuminated part of the disk, first at the Lick Observatory, then by Perrotin of Nice, and then by other observers. English readers heard of it first in the issue of _Nature_ dated August 2. I am inclined to think that this blaze may have been the casting of the huge gun, in the vast pit sunk into their planet, from which their shots were fired at us. Peculiar markings, as yet unexplained, were seen near the site of that outbreak during the next two oppositions.",
    "A singularly appropriate phrase it proved. Yet the next day there was nothing of this in the papers except a little note in the _Daily Telegraph_, and the world went in ignorance of one of the gravest dangers that ever threatened the human race. I might not have heard of the eruption at all had I not met Ogilvy, the well-known astronomer, at Ottershaw. He was immensely excited at the news, and in the excess of his feelings invited me up to take a turn with him that night in a scrutiny of the red planet.",
    "The end."
]

# Generate metrics by randomly translating different text segments
# Randomly select different sized segments to different languages
i = 0
while i < 10000:
    i += 1
    translate_text(
        random.choice(text_segments),
        random.choice(['es', 'de', 'pt'])
    )
    time.sleep(1)
