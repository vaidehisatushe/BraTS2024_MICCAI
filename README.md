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

# Fetch the code from GitHub
git clone https://github.com/mlcommons/mlcube_examples && cd ./mlcube_examples
git fetch origin pull/65/head:feature/getting_started && git checkout feature/getting_started
cd ./getting_started/mlcube

