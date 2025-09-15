# This code converts the label to the int.
from dataset.get_dataset import get_dataset

dataset = get_dataset()

label_map = {
        # anger
        "angry": 0, "ANG": 0, "anger": 0,

        # disgust
        "disgust": 1, "DIS": 1,

        # fear
        "fearful": 2, "FEA":
          2, "fear": 2,

        # happiness
        "happiness": 3, "happy": 3, "HAP": 3,

        # sadness
        "sadness": 4, "sad": 4, "SAD": 4,

        # surprise
        "surprise": 5, "surprised": 5,

        # neutral
        "neutral": 6, "NEU": 6,

        # calm (special case, only Ravdess has it)
        "calm": 7,
    }

def processed_dataset():

    sety = set()
    for key, value in dataset.items():
        for i in value:
            sety.add(i["label"])

    for category in dataset:
        for item in dataset[category]:
            label_str = item["label"]
            if label_str in label_map:
                item["label"] = label_map[label_str]
            elif label_str == "ps":
                item["label"] = 5
            else:
                print(f"Warning: Unknown label '{label_str}' in category '{category}'")
    return dataset