import os 
import glob
from dataset.path_to_dataset import path

path = path()

def get_wav_files():

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
    categories = os.listdir(path)

    wav_by_categories = {}

    for category in categories: 
        category_path = os.path.join(path, category)

        wav_files = glob.glob(os.path.join(category_path, "**", "*.wav"), recursive=True)

        wav_by_categories[category] = wav_files

    return categories, wav_by_categories




