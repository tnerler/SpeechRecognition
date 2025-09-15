from dataset.str_to_int import processed_dataset
import pandas as pd 


dataset = processed_dataset()

int_to_str = {
    0: "anger",
    1: "disgust",
    2: "fear",
    3: "happiness",
    4: "sadness",
    5: "surprise",
    6: "neutral",
    7: "calm"
}

def get_df():

    rows = []
    for key, value in dataset.items(): 
        for i in value: 
            rows.append({
                "Categories": key,
                "path": i["file_path"],
                "label": i["label"],
                "str_label": int_to_str[i["label"]]
            })

    wav_dataframe = pd.DataFrame(rows)
    
    return wav_dataframe

dataset = get_df()
print(dataset.head())