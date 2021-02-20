import csv

from gtts import gTTS
from deep_translator import GoogleTranslator

VOICE_LANG = 'ca'
SOURCE_LANG = 'en'
DESTINATION_LANG = 'fa'
SENTENCES_FILE = 'sentences.txt'
SENTENCES_OUTPUT_FILE = 'sentences.txt.csv'


def sentence_normalizer(text: str) -> str:
    _sentence = text.strip().lower()
    if not _sentence.endswith('.'):
        _sentence = _sentence + '.'

    return _sentence


if __name__ == '__main__':
    with open(SENTENCES_OUTPUT_FILE, 'w', newline='\n') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

        for sentence in open(SENTENCES_FILE).readlines():
            sentence = sentence_normalizer(sentence)
            tts = gTTS(sentence, lang=SOURCE_LANG, tld=VOICE_LANG)
            tts.save(f'{sentence.lower().replace(" ", "_").replace(".", "")}.mp3')

            translated = GoogleTranslator(source=SOURCE_LANG, target=DESTINATION_LANG).translate(sentence)
            writer.writerow([sentence, translated])
