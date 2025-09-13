import os 
from dataset.audio_dict import get_wav_files

"""
### Crema:

The third component is responsible for the emotion 
label:

SAD - sadness;
ANG - angry;
DIS - disgust;
FEA - fear;
HAP - happy;
NEU - neutral.
"""

"""
### Ravdess:


Here is the filename identifiers as per the official RAVDESS website:

Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
Vocal channel (01 = speech, 02 = song).
Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.
Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").
Repetition (01 = 1st repetition, 02 = 2nd repetition).
Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).
So, here's an example of an audio filename. 02-01-06-01-02-01-12.wav This means the meta data for the audio file is:

Video-only (02)
Speech (01)
Fearful (06)
Normal intensity (01)
Statement "dogs" (02)
1st Repetition (01)
12th Actor (12) - Female (as the actor ID number is even)
"""


"""
Savee:

The audio files in this dataset are named in such a way that the prefix letters describes the emotion classes as follows:

'a' = 'anger'
'd' = 'disgust'
'f' = 'fear'
'h' = 'happiness'
'n' = 'neutral'
'sa' = 'sadness'
'su' = 'surprise'
"""

"""
Tess:

Very similar to Crema - label of emotion is contained in the name of file.
It is gonna be our test dataset.
"""

# 'C:\\Users\\Tuana\\.cache\\kagglehub\\datasets\\dmitrybabko\\speech-emotion-recognition-en\\versions\\1\\Crema\\1091_WSI_SAD_XX.wav'


categories, wav_files = get_wav_files()

def extract_crema_label(filename):
    return filename.split("_")[2]


def extract_ravdess_label(filename):
    label_map = {"01" : "neutral", "02" : "calm", "03" : "happy", "04" : "sad", "05" : "angry", "06" : "fearful", "07" : "disgust", "08" : "surprised"}
    emotion = label_map[filename.split("-")[2]]
    return emotion

def extract_savee_label(filename):
    label_map = {'a' : 'anger',
                 'd' : 'disgust',
                 'f' : 'fear',
                 'h' : 'happiness',
                 'n' : 'neutral',
                 'sa': 'sadness',
                 'su': 'surprise'}
    a = filename.split("_")[1]
    b = a.split(".")[0]
    
    for key, value in label_map.items():
        if b.startswith(key): 
            return label_map[key]

# ['DC_a01.wav']

def extract_tess_label(filename):
    emotion_side = filename.split("_")[2]
    
    emotion = emotion_side.split(".")[0]
    return emotion


extractors = {
    "Crema": extract_crema_label,
    "Ravdess": extract_ravdess_label,
    "Savee": extract_savee_label,
    "Tess": extract_tess_label
}

def get_dataset():

    datasets = {"Crema": [], "Ravdess": [], "Savee": [], "Tess": []}
    for key, value in wav_files.items():
        if key in datasets: 
            for file_path in value:
                file_name = os.path.basename(file_path)
                label = extractors[key](file_name)
                datasets[key].append({
                    "file_path": file_path,
                    "label": label
                })
    return datasets

# print(datasets["Crema"])
# print(datasets["Ravdess"][:1]) 
# print(datasets["Savee"][:1]) 
# print(datasets["Tess"][:1]) 

"""

['1090_IWL_HAP_XX.wav']
['03-01-01-01-01-01-01.wav']
['DC_a01.wav']
['OAF_back_angry.wav']
"""





