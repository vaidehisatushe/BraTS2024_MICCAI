# Use the official TensorFlow image as a base
FROM tensorflow/tensorflow:2.12.0-gpu

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-opencv \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    git \
    wget

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install \
    nibabel \
    matplotlib \
    scikit-learn \
    pandas \
    opencv-python-headless \
    tensorflow-addons \
    jupyter \
    Pillow

# Optional: Install Jupyter Notebook
RUN pip install notebook

# Set environment variables for TensorFlow
ENV TF_FORCE_GPU_ALLOW_GROWTH=true

# Command to run Jupyter Notebook
#CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]

# Optional: Uncomment the next line if you want to run a specific Python script on container start
CMD ["python", "BraTS-GoAT2024 NNUNet Model Complete Updated.py"]