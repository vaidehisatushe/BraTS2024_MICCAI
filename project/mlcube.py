# mlcube.py

from infer import infer
import os

# Paths to the main directories
validation_base_dir = '/mlcube/workspace/data/MICCAI2024-BraTS-GoAT-ValidationData/'
training_base_dir = '/mlcube/workspace/data/MICCAI2024-BraTS-GoAT-TrainingData-With-GroundTruth/'
save_dir = 'mlcube/workspace/additional_files/Segmentation_Results'

# List the folders in each directory
validation_folders = sorted(os.listdir(validation_base_dir))
training_folders = sorted(os.listdir(training_base_dir))

# Check if there are enough training folders
if len(training_folders) < len(validation_folders):
    raise ValueError("Not enough training folders to match the validation folders.")

# Create the folder mapping
folder_mapping = {}
for i, val_folder in enumerate(validation_folders):
    folder_mapping[val_folder] = training_folders[i]

# Optionally, print the mapping
for val_folder, train_folder in folder_mapping.items():
    print(f"{val_folder} -> {train_folder}")

# Now, `folder_mapping` contains the mapping of each validation folder to a corresponding training folder.

if __name__ == "__main__":
    infer(validation_base_dir, training_base_dir, save_dir, folder_mapping)
