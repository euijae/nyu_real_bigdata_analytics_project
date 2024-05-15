import os

# Import necessary libraries for pipeline and accuracy calculation
from transformers import pipeline
import torch
from tqdm import tqdm
# Load your model pipeline
video_cls = pipeline(model="devd-99/videomae-base-finetuned-ucf101-subset")  # Adjust 'device' if using a GPU

# Path to your test dataset
dataset_root_path = './dataset/test'
class_folders = ['made', 'missed']

correct_predictions = 0
total_predictions = 0

with open("predictions_table.csv", "w") as f:
    f.write("Predicted,Actual\n")  # Write the header
# Iterate over each class folder
    for class_folder in tqdm(class_folders, desc='Class Folders'):
        folder_path = os.path.join(dataset_root_path, class_folder)
        # List all video files in the directory
        video_files = [file for file in os.listdir(folder_path) if file.endswith('.mp4')]
        
        # Predict the class for each video using tqdm for progress
        for video_file in tqdm(video_files, desc=f'Processing {class_folder}'):
            video_path = os.path.join(folder_path, video_file)
            predictions = video_cls(video_path)
            
            # Get the predicted class with the highest score
            predicted_class = max(predictions, key=lambda x: x['score'])['label']
            
            # Write the prediction and actual class to the file
            f.write(f"{predicted_class},{class_folder}\n")
            
            # Check if the prediction matches the true class
            if predicted_class == class_folder:
                correct_predictions += 1
            total_predictions += 1

# Calculate the accuracy
accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
print(f"Accuracy: {accuracy:.2f}")