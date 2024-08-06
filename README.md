Important files
These are the most important files on this project:

├── mlcube
│   ├── mlcube.yaml          # MLCube configuration, defines the project, author, platform, docker and tasks.
│   └── workspace            # This folder is mounted at runtime. Note that it will be empty during fed. eval.
│       ├── data             # For example some data can be put here during local testing.
│       └── output           # Location where inference outputs are stored.
└── project
    ├── Dockerfile           # Docker file with instructions to create the image.
    ├── BraTS-GoAT2024 NNUNet Model Complete Updated.py            # Python entrypoint used by MLCube, contains the logic for MLCube tasks.
    ├── parameters.yaml      # File with parameters used by inference procedure.
    ├── requirements.txt     # Python requirements needed to run the project inside Docker.


Dockerize the project
We'll create a Dockerfile with the needed steps to run the project, at the end we'll need to define the execution of the mlcube.py file as the entrypoint. This file will be located in project/Dockerfile.

This file is already provided, please take a look and study its content.

When creating the docker image, we'll need to run the docker build command inside the project folder, the command that we'll use is:

docker build . -t mlcommons/getting_started:0.0.1 -f Dockerfile

Keep in mind the tag that we just described.

Define MLCube files
Inside the mlcube folder we'll need to define the following files.

MLCube parameters file
We can use the mlcube/workspace/parameters.yaml file to describe all the input parameters we'll use (this file is already provided, please take a look and study its content), the idea is to describe all the parameters in this file and then use this single file as an input for the task. Then we can read the content of the parameters file in Python to pass these to our logic.

MLCube task definition file
The file located in mlcube/mlcube.yaml contains the definition of all the tasks and their parameters.

This file is already provided, please take a look and study its content.

With this file we have finished the packing of the project into MLCube! Now we can setup the project and run all the tasks.

Project setup
# Create Python environment and install MLCube Docker runner 
virtualenv -p python3 ./env && source ./env/bin/activate && pip install mlcube-docker

# Fetch the boston housing example from GitHub
git clone https://github.com/mlcommons/mlcube_examples && cd ./mlcube_examples
git fetch origin pull/65/head:feature/getting_started && git checkout feature/getting_started
cd ./getting_started/mlcube
Dataset
The Boston Housing Dataset will be downloaded and processed. Sizes of the dataset in each step:

Dataset Step	MLCube Task	Format	Size
Downlaod (Compressed dataset)	download_data	txt file	~52 KB
Preprocess (Processed dataset)	preprocess_data	csv file	~40 KB
Total	(After all tasks)	All	~92 KB
Tasks execution
# Download Boston housing dataset. Default path = /workspace/data
# To override it, use data_dir=DATA_DIR
mlcube run --task download_data

# Preprocess Boston housing dataset, this will convert raw .txt data to .csv format
# It will use the data from the DATA_DIR path defined in the previous step
mlcube run --task preprocess_data

# Run training.
# Parameters to override: dataset_file_path=DATASET_FILE_PATH parameters_file=PATH_TO_TRAINING_PARAMS
mlcube run --task train
To execute all pipeline with one single command, use this:

mlcube run --task=download_data,preprocess_data,train
MLCube Command
We are targeting pull-type installation, so MLCube images should be available on docker hub. If not, try this:

mlcube run ... -Pdocker.build_strategy=always
Parameters defined in mlcube.yaml can be overridden using: param=input, example:

mlcube run --task=download_data data_dir=absolute_path_to_custom_dir
Also, users can override the workspace directory by using:

mlcube run --task=download_data --workspace=absolute_path_to_custom_dir
Note: Sometimes, overriding the workspace path could fail for some task, this is because the input parameter parameters_file should be specified, to solve this use:

mlcube run --task=train --workspace=absolute_path_to_cus
