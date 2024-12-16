import time

from gtts import gTTS as GTTS


GTTS.GOOGLE_TTS_MAX_CHARS = 400

def text2sound(text:str, language:str='en') -> None:
    ctime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    obj = GTTS(text=text, lang=language, slow=False)
    obj.save(f'test_{ctime}.mp3')


if __name__ == '__main__':
    text2sound('Hello, world!')