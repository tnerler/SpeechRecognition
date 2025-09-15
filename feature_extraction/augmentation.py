import random

import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from dataset.str_to_int import processed_dataset
from dataset.audio_dict import get_wav_files

dataset = processed_dataset()
_, wav = get_wav_files()
### Noise
def noise(data):
    noise_amp = 0.050 * np.random.uniform() * np.amax(data)
    data = data + noise_amp * np.random.normal(size=data.shape[0])
    return data
### Stretch
def stretch(data, rate=0.9):
    return librosa.effects.time_stretch(data, rate=rate)

### Shift
def shift(data):
    shift_range = int(np.random.uniform(low=-2, high=2) * 1000)
    return np.roll(data, shift_range)

### Combined Augmentation Function

def augment_audio(data, sr):
    augmentations = [noise, stretch, shift]
    applied_augs = random.sample(augmentations, random.randint(1, 3))

    for augmentation in applied_augs:
        data = augmentation(data)
    return data
