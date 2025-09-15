from tqdm import tqdm
from dataset.pd_dataset import get_df
from feature_extraction.preprocess import preprocess_audio_aug, preprocess_audio_n
import librosa 

df = get_df()
print(df.head())


def get_emotion_list(): 
    """
    # ZCR – Zero Crossing Rate
    Meausre how noisy the audio is\n
    High ZCR --> noisy, unvoiced, or fricative sounds (like “s”, “f”).\n
    Low ZCR → voiced, stable sounds (like vowels “a”, “o”).

    # RMS - Root Mean Square Energy
    Measures the loudness(energy) of the sound\n
    High RMS → loud speech, shouting, strong emotions.\n
    Low RMS → quiet speech, silence, soft emotions.

    # MFCC – Mel-Frequency Cepstral Coefficients
    A set of features that describe the shape of the sound spectrum but on a scale closer to human hearing (the mel scale)\n

    * ZCR → noisiness
    * RMS → loudness
    * MFCC → voice tone/character
    """
    zcr_list = []
    rms_list = []
    mfccs_list = []
    emotion_list = []

    FRAME_LENGTH = 400
    HOP_LENGTH = 160
    sr = 16000
    
    # 25 ms / 10 ms 

    for row in tqdm(df.itertuples(index=False)):
        try: 
            
            y, _ = preprocess_audio_n(row.path)
            
            zcr = librosa.feature.zero_crossing_rate(y, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH)
            rms = librosa.feature.rms(y, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH)
            mfccs = librosa.feature.mfcc(y, sr=sr, n_mfcc=20, hop_length=HOP_LENGTH)
            
            zcr_list.append(zcr)
            rms_list.append(rms)
            mfccs_list.append(mfccs)

            emotion_list.append(row.label) # int label

            y, _ = preprocess_audio_aug(row.path)

            zcr = librosa.feature.zero_crossing_rate(y, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH)
            rms = librosa.feature.rms(y, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH)
            mfccs = librosa.feature.mfcc(y, sr=sr, n_mfcc=20, hop_length=HOP_LENGTH)

            zcr_list.append(zcr)
            rms_list.append(rms)
            mfccs_list.append(mfccs)

            emotion_list.append(row.label)

        except:
            print(f"Failed for path: {row.path}")  
    return zcr_list, mfccs_list, rms_list

