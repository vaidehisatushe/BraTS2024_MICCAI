# data_loader.py

import os
import nibabel as nib
import numpy as np

def load_images(base_dir, folder_name):
    file_paths = {
        "t1c": os.path.join(base_dir, f"{folder_name}-t1c.nii.gz"),
        "t1n": os.path.join(base_dir, f"{folder_name}-t1n.nii.gz"),
        "t2f": os.path.join(base_dir, f"{folder_name}-t2f.nii.gz"),
        "t2w": os.path.join(base_dir, f"{folder_name}-t2w.nii.gz")
    }
    images = {key: nib.load(file_paths[key]).get_fdata().astype(np.float32) for key in file_paths}
    return images

def load_segmentation(segmentation_path):
    segmentation_image = nib.load(segmentation_path).get_fdata().astype(np.uint8)
    corrected_segmentation_image = np.zeros((240, 240, 155), dtype=np.uint8)
    corrected_segmentation_image[:, :, :segmentation_image.shape[2]] = segmentation_image
    return corrected_segmentation_image

def save_segmentation(segmentation, affine, save_path):
    nib.save(nib.Nifti1Image(segmentation, affine), save_path)

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
