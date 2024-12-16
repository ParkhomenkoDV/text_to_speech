import time

import torch
import sounddevice as sd

from gtts import gTTS as GTTS


def text2sound(text: str, language: str = 'en') -> None:
    ctime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    if len(text) < GTTS.GOOGLE_TTS_MAX_CHARS: GTTS.GOOGLE_TTS_MAX_CHARS = len(text)
    obj = GTTS(text=text, lang=language, slow=False)
    obj.save(f'test_{ctime}.mp3')


class TTS:
    MODEL_ID = ('v3_1_ru', 'ru_v3', 'aidar_v2', 'aidar_8khz', 'aidar_16khz', 'baya_v2', 'baya_8khz', 'baya_16khz',
                'irina_v2', 'irina_8khz', 'irina_16khz', 'kseniya_v2', 'kseniya_8khz', 'kseniya_16khz', 'natasha_v2',
                'natasha_8khz', 'natasha_16khz', 'ruslan_v2', 'ruslan_8khz', 'ruslan_16khz', 'v3_en', 'v3_en_indic',
                'lj_v2', 'lj_8khz', 'lj_16khz', 'v3_de', 'thorsten_v2', 'thorsten_8khz', 'thorsten_16khz', 'v3_es',
                'tux_v2', 'tux_8khz', 'tux_16khz', 'v3_fr', 'gilles_v2', 'gilles_8khz', 'gilles_16khz', 'aigul_v2',
                'v3_xal', 'erdni_v2', 'v3_tt', 'dilyara_v2', 'v3_uz', 'dilnavoz_v2', 'v3_ua', 'mykyta_v2', 'v3_indic',
                'multi_v2',)

    SPEAKERS = ('aidar', 'baya', 'kseniya', 'xenia', 'random')

    __slots__ = ('model', 'speaker', 'accent', 'yo')

    def __init__(self, language: str, model_id: str,
                 repo_or_dir: str = 'snakers4/silero-models', model: str = 'silero_tts',
                 speaker: str = 'random', accent: bool = True, yo: bool = True):
        torch_model, _ = torch.hub.load(repo_or_dir=repo_or_dir, model=model,
                                        language=language, speaker=model_id)
        device = torch.device('cpu')  # cpu или gpu
        torch_model.to(device)

        self.model = torch_model
        self.speaker: str = speaker
        self.accent: bool = accent
        self.yo: bool = yo

    @staticmethod
    def preprocessing(text: str):
        if text[-1] not in '.!?': text += '.'
        return text

    def to_array(self, text: str, sample_rate: int = 48_000):
        text = self.preprocessing(text)
        return self.model.apply_tts(text=text,
                                    sample_rate=sample_rate,
                                    speaker=self.speaker,
                                    put_accent=self.accent,
                                    put_yo=self.yo)

    def play(self, text: str, sample_rate: int):
        """Воспроизведение аудиодорожки из массива"""
        arr = self.to_array(text, sample_rate)
        sd.play(arr, sample_rate)
        time.sleep(len(arr) / sample_rate + 0.2)
        sd.stop()


if __name__ == '__main__':
    language = 'ru'
    model_id = 'ru_v3'
    speaker = 'xenia'
    tts = TTS(language=language, model_id=model_id, speaker=speaker)

    text = "Тестирование голоса."
    sample_rate = 48_000
    tts.play(text, sample_rate)
