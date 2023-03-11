import os.path
import pdfplumber
from gtts import gTTS
import gtts


def check_file_exists(path: str) -> bool:
    if not os.path.isfile(path):
        print("[x]File not exist")
        return False
    return True


def get_filename_and_extension(path: str) -> tuple:
    return os.path.splitext(path)


def check_file_extension(path: str) -> bool:
    extensions_lst = ['.pdf', '.txt']
    extension = get_filename_and_extension(path)[1]
    if extension not in extensions_lst:
        print("[x]Check file extension")
        return False
    return True


def check_language(lang: str) -> bool:
    lang_lst = gtts.lang.tts_langs().keys()
    if lang not in lang_lst:
        print("[x]Incorrect language")
        return False
    return True


def read_file(path: str) -> str:
    _, extension = get_filename_and_extension(path)

    if extension == '.pdf':
        with pdfplumber.open(path) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages)
            # when pdfplumber convert pdf into string its problem with russian letter 'к' it convert as unicode 312 symbol
            text = text.replace(chr(312), 'к')

    elif extension == '.txt':
        with open(path, 'r') as file:
            text = file.read()

    else:
        text = ''
    text = text.replace('\n', '')
    print("[*]Processing")
    return text


def convert_file_to_mp3(path: str, lang='en') -> None:
    if not check_file_exists(path):
        return
    if not check_file_extension(path):
        return
    text = read_file(path)
    if not check_language(lang):
        return

    filename, _ = get_filename_and_extension(path)
    # get voice and save it in file with the same filename
    tts = gTTS(text, lang=lang)
    tts.save(filename+'.mp3')
    print("[*]File was saved successfully")


if __name__ == '__main__':
    print('[*]Input file path')
    path = input()
    print('[*]Input language')
    lang = input()
    convert_file_to_mp3(path, lang)
