## This is end to end deep learning project

# 1. Creating the structure for the project
- Creating the folder and files including:
1. requirements.txt, setup.py ...
2. src (source): components, pipeline, entity, config, constant, utils, ...
3. research(ipynb): the testing code phase
4. .yaml files (config, params, dvc ...)

# 2. Set up environments and requirements installation
1. Updating setup.py
2. Updating requirements.txt
3. Building virtual environments

# 3. Logger, exception and utils
1. Setting up custom log
2. Adding all the common function in utils

# THE PROCEDURE OF PROJECT CONTAINS:
- DATA INGESTION
- PREPARE BASE MODEL
- PREPARE CALLBACKS
- MODEL TRAINER
- MODEL EVALUATION
- PREDICTION

# 4 Proceed the workflow repeatedly for each part
1. Update config.yaml
2. Update params.yaml 
- After 2 steps at first time we did, updating the constant file !!!
3. Update the entity
4. Update the configuration in config
5. update the components
6. update the pipeline
7. update the main.py
8. update the dvc.yaml

# 5. Apply DVC to track the pipeline
- DVC file includes all stages of the pipelines. Each stage contains: cmd, dependencies, outputs

# 6. Create an web application using API (Flask)
- Create an .html file in an templates folder

# 7. CICD project deployment on AWS/Azure
Apply EC2 and ECR
The steps to deploy:

- 7.1. Create IAM user
Apply 2 policies: 
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

- 7.2. Create ECR repo

- 7.3. Create EC2

- 7.4. Install docker in EC2 Machine:
1. sudo apt-get update -y
2. sudo apt-get upgrade
3. curl -fsSL https://get.docker.com -o get-docker.sh
4. sudo sh get-docker.sh
5. sudo usermod -aG docker ubuntu
6. newgrp docker

- 7.5. Config EC2

- 7.6. Secrets key in github
1. AWS_ACCESS_KEY_ID
2. AWS_SECRET_ACCESS_KEY
3. AWS_REGION 
4. AWS_ECR_LOGIN_URI 
5. ECR_REPOSITORY_NAME 





