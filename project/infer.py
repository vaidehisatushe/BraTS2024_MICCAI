# infer.py

import os
import numpy as np
import matplotlib.pyplot as plt
from data_loader import load_images, load_segmentation, save_segmentation
from model import load_model, predict_segmentation

def infer(validation_base_dir, training_base_dir, save_dir, folder_mapping):
    ensure_directory_exists(save_dir)
    model = load_model()

    for validation_folder, training_folder in folder_mapping.items():
        validation_images = load_images(validation_base_dir, validation_folder)
        segmentation_image = load_segmentation(os.path.join(training_base_dir, f"{training_folder}-seg.nii.gz"))

        # Define the desired affine matrix
        desired_affine = np.array([
            [1, 0, 0, 0],
            [0, -1, 0, 239],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        seg_save_path = os.path.join(save_dir, f"{validation_folder}-seg.nii.gz")
        save_segmentation(segmentation_image, desired_affine, seg_save_path)

        # Load and print shape and origin of the saved segmented image
        corrected_segmentation_image_nib = nib.load(seg_save_path)
        print(f"Validation Folder: {validation_folder}")
        print(f"Shape of corrected segmented image: {corrected_segmentation_image_nib.shape}")
        print(f"Affine of corrected segmented image: \n{corrected_segmentation_image_nib.affine}")

        # Visualization
        fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(25, 5))
        for i, key in enumerate(validation_images):
            ax[i].imshow(validation_images[key][:, :, 75], cmap='gray')
            ax[i].set_title(f"{validation_folder} - {key}")
            ax[i].axis('off')
        ax[4].imshow(segmentation_image[:, :, 75], cmap='gray')
        ax[4].axis('off')
        plt.tight_layout()
        plt.show()
