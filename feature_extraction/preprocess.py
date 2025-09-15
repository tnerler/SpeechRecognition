import librosa
from feature_extraction.augmentation import augment_audio
import numpy as np

def preprocess_audio_aug(path): 
    audio, sr = librosa.load(path, sr=16000)
    trimmed, _ = librosa.effects.trim(audio, top_db=30, frame_length=256, hop_length=64)
    audio = augment_audio(trimmed, sr)
    audio_dur = len(audio) / sr

    if audio_dur > 4: 
        audio = audio[:4*sr]
    else: 
        audio = np.pad(audio, (0, (4*sr)-len(audio)), "constant")
    
    return audio, sr

def preprocess_audio_n(path): 
    audio, sr = librosa.load(path, sr=16000)
    audio, _ = librosa.effects.trim(audio, top_db=30, frame_length=256, hop_length=64)
    audio_dur = len(audio) / sr

    if audio_dur > 4: 
        audio = audio[:4*sr]
    else: 
        audio = np.pad(audio, (0, (4*sr)-len(audio)), "constant")
    
    return audio, sr