import os
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from data_loader import load_images, load_segmentation, save_segmentation
from model import load_model, predict_segmentation


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def infer(data_path, output_path):
    ensure_directory_exists(output_path)
    model = load_model()

    # List all validation folders in the data_path
    validation_folders = sorted(os.listdir(data_path))

    for validation_folder in validation_folders:
        # Assuming the training segmentation file has the same name as the validation folder
        validation_images = load_images(os.path.join(data_path, validation_folder))
        # Predict the segmentation using the loaded model
        predicted_segmentation = predict_segmentation(model, validation_images)

        # Define the desired affine matrix
        desired_affine = np.array([
            [1, 0, 0, 0],
            [0, -1, 0, 239],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        # Save the predicted segmentation
        seg_save_path = os.path.join(output_path, f"{validation_folder}-pred-seg.nii.gz")
        save_segmentation(predicted_segmentation, desired_affine, seg_save_path)

        # Load and print shape and origin of the saved predicted segmentation image
        predicted_segmentation_image_nib = nib.load(seg_save_path)
        print(f"Validation Folder: {validation_folder}")
        print(f"Shape of predicted segmented image: {predicted_segmentation_image_nib.shape}")
        print(f"Affine of predicted segmented image: \n{predicted_segmentation_image_nib.affine}")

        # Visualization
        fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(25, 5))
        for i, key in enumerate(validation_images):
            ax[i].imshow(validation_images[key][:, :, 75], cmap='gray')
            ax[i].set_title(f"{validation_folder} - {key}")
            ax[i].axis('off')
        ax[4].imshow(predicted_segmentation[:, :, 75], cmap='gray')
        ax[4].set_title(f"{validation_folder} - Pred Segmentation")
        ax[4].axis('off')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    data_path = "pseudo_val_set"
    output_path = "pseudo_val_output"

    infer(data_path, output_path)
