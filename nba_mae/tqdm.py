import os

# Import necessary libraries for pipeline and accuracy calculation
from transformers import pipeline
import torch
from tqdm import tqdm
# Load your model pipeline
video_cls = pipeline(model="devd-99/videomae-base-finetuned-ucf101-subset")  # Adjust 'device' if using a GPU

# Path to your test dataset
dataset_root_path = './m2/train'
class_folders = ['made', 'missed']

correct_predictions = 0
total_predictions = 0

with open("predictions_table.csv", "w") as f:

    f.write("Video_File, Predicted_class, Actual_Class, Confidence\n")  # Write the header
# Iterate over each class folder
    for class_folder in tqdm(class_folders, desc='Class Folders'):
        folder_path = os.path.join(dataset_root_path, class_folder)
        # List all video files in the directory
        video_files = [file for file in os.listdir(folder_path) if file.endswith('.mp4')]

        # Predict the class for each video using tqdm for progress
        for video_file in tqdm(video_files, desc=f'Processing {class_folder}'):
            video_path = os.path.join(folder_path, video_file)
            predictions = video_cls(video_path)

            print(predictions)
            max_score = -1
            max_label = ""
            for pred in predictions:
                if(pred['score']):
                    if(pred['score']> max_score):
                        max_score = pred['score']
                        max_label = pred['label']

            

            # # Write the prediction and actual class to the file
            # f.write(f"{predicted_class},{class_folder}\n")

            # Check if the prediction matches the true class
            if max_label == class_folder:
                correct_predictions += 1
            total_predictions += 1


           

            # Write results to CSV
            f.write({f" {video_file}, {max_label}, {class_folder}, {max_score}\n "
                 # Store the logits
            })

# Calculate the accuracy
accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
print(f"Accuracy: {accuracy:.2f}")