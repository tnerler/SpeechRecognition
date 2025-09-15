# train, val, test

# Savee dataset will be the test dataset.
# Validation dataset of 500 audio files from Crema.
# The rest of it, it will be train dataset.

from dataset.str_to_int import processed_dataset
import random

random.seed(42)

dataset = processed_dataset()

crema = dataset["Crema"]
savee = dataset["Savee"]
tess = dataset["Tess"]
ravdess = dataset["Ravdess"]

random.shuffle(crema)
random.shuffle(tess)
random.shuffle(ravdess)

val_size = 500

total_count = len(crema) + len(tess) + len(savee) + len(ravdess)
crema_val_size = int(len(crema) / total_count * val_size)
tess_val_size = int(len(tess) / total_count * val_size)
ravdess_val_size = val_size - (crema_val_size + tess_val_size)

val_set = (
    crema[:crema_val_size] + 
    tess[:tess_val_size] + 
    ravdess[:ravdess_val_size]
)

train_set = (
    crema[crema_val_size:] + 
    tess[tess_val_size:] + 
    ravdess[ravdess_val_size:]
)

test_set = savee

print(f"Train: {len(train_set)} samples")
print(f"Validation: {len(val_set)} samples")
print(f"Test: {len(test_set)} samples")
