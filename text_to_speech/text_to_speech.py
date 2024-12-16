import torch

from play_sound import play_sound


def va_speak(text: str, speaker: str, sample_rate: int, put_accent: bool, put_yo: bool):
    """Воспроизведение"""
    audio = model.apply_tts(text=text + "..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    play_sound(audio, sample_rate)


if __name__ == '__main__':
    language = 'ru'
    model_id = 'ru_v3'

    """
    ['v3_1_ru', 'ru_v3', 'aidar_v2', 'aidar_8khz', 'aidar_16khz', 'baya_v2', 'baya_8khz', 'baya_16khz', 
    'irina_v2', 'irina_8khz', 'irina_16khz', 'kseniya_v2', 'kseniya_8khz', 'kseniya_16khz', 'natasha_v2', 
    'natasha_8khz', 'natasha_16khz', 'ruslan_v2', 'ruslan_8khz', 'ruslan_16khz', 'v3_en', 'v3_en_indic', 
    'lj_v2', 'lj_8khz', 'lj_16khz', 'v3_de', 'thorsten_v2', 'thorsten_8khz', 'thorsten_16khz', 'v3_es', 
    'tux_v2', 'tux_8khz', 'tux_16khz', 'v3_fr', 'gilles_v2', 'gilles_8khz', 'gilles_16khz', 'aigul_v2', 
    'v3_xal', 'erdni_v2', 'v3_tt', 'dilyara_v2', 'v3_uz', 'dilnavoz_v2', 'v3_ua', 'mykyta_v2', 'v3_indic',
    'multi_v2']
    """
    
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)
    device = torch.device('cpu')  # cpu или gpu
    model.to(device)

    text = "Тестирование голоса"
    sample_rate = 48_000
    speaker = 'baya'  # aidar, baya, kseniya, xenia, random
    put_accent = True
    put_yo = True

    va_speak(text, 
             speaker=speaker, 
             sample_rate=sample_rate,
             put_accent=put_accent,
             put_yo=put_yo)
