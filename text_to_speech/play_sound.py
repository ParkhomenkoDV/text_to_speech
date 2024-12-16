import time

import sounddevice as sd


def play_sound(sound, sample_rate: int):
    sd.play(sound, sample_rate * 1.05)
    time.sleep((len(sound) / sample_rate) + 0.5)
    sd.stop()


if __name__ == '__main__':
    import os 

    for file in os.listdir():
        if file.endswith(".mp3"):
            play_sound(file, 48_000)
            break