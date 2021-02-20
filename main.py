import csv

from gtts import gTTS
from deep_translator import GoogleTranslator


def normalize_sentence(text: str) -> str:
    _sentence = text.strip().lower()
    if not _sentence.endswith('.'):
        _sentence = _sentence + '.'

    return _sentence


with open('sentences.txt.csv', 'w', newline='\n') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    for sentence in open('sentences.txt').readlines():
        sentence = normalize_sentence(sentence)
        tts = gTTS(sentence, lang='en', tld='ca')
        tts.save(f'{sentence.lower().replace(" ", "_").replace(".", "")}.mp3')

        translated = GoogleTranslator(source='en', target='fa').translate(sentence)
        writer.writerow([sentence, translated])
