import os
import shutil
import random

def create_split_dirs(base_dir, categories):
    # Create train, test, val directories with subdirectories for each category
    for split in ['train', 'test', 'val']:
        for category in categories:
            os.makedirs(os.path.join(base_dir, split, category), exist_ok=True)

def split_data(base_dir, category, train_ratio, test_ratio):
    # List all files in the category directory
    source_dir = os.path.join(base_dir, category)
    files = os.listdir(source_dir)
    random.shuffle(files)

    # Compute split indices
    n_total = len(files)
    n_train = int(n_total * train_ratio)
    n_test = int(n_total * test_ratio)
    n_val = n_total - n_train - n_test

    # Assign files to train, test, and val sets
    train_files = files[:n_train]
    test_files = files[n_train:n_train + n_test]
    val_files = files[n_train + n_test:]

    # Function to copy files to destination folder
    def copy_files(files, split):
        for file in files:
            shutil.move(os.path.join(source_dir, file),
                        os.path.join(base_dir, split, category, file))

    # Move files to corresponding folders
    copy_files(train_files, 'train')
    copy_files(test_files, 'test')
    copy_files(val_files, 'val')

def distribute_files(base_dir, categories, train_ratio=0.7, test_ratio=0.2):
    create_split_dirs(base_dir, categories)
    for category in categories:
        split_data(base_dir, category, train_ratio, test_ratio)

# Usage
base_directory = './dataset'  # Change to your dataset path
categories = ['made', 'missed']
distribute_files(base_directory, categories)
