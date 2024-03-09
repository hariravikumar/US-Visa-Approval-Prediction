**US Visa Approval Prediction**


**🔍 Description for US Visa Approval Prediction for Machine Learning Model - MLOps Project:**

The US Visa Approval Prediction project aims to develop a machine learning model that can accurately predict the approval or rejection of US visa applications. This project adopts a modular coding approach, leveraging various technologies to build an end-to-end solution. The primary technologies used in this project include:

**🐍 Python:** Python, a versatile and widely-used programming language for machine learning, is employed for data preprocessing, feature engineering, and model development.

**📓 Jupyter Notebook:** Jupyter Notebook provides an interactive and collaborative environment to explore and analyze the data, experiment with different algorithms, and fine-tune the model parameters.

**🖥️ Visual Studio Code:** Visual Studio Code, a powerful integrated development environment (IDE), is utilized for writing modular and scalable code. It enables efficient coding practices, debugging, and version control integration with Git, ensuring better collaboration among team members.

**🍃 MongoDB:** MongoDB, a NoSQL document database, is used to store and manage the visa application data. It provides flexibility and scalability for handling large datasets efficiently.

**🐙 GitHub:** GitHub serves as the version control and collaboration platform, allowing team members to work together, track changes, and manage the project's codebase effectively.

**⚡ FastAPI:**  FastAPI, a modern web framework for building APIs, is used to create a robust and scalable API for serving the machine learning model predictions. It offers high performance and automatic documentation generation.

**☁️ AWS S3:**  AWS S3 (Simple Storage Service) is utilized for storing and managing the dataset and other project-related files. It provides secure and scalable cloud storage for easy accessibility and data sharing.

By combining these technologies, the US Visa Approval Prediction project aims to develop a reliable and efficient machine learning model that can assist in predicting the outcome of US visa applications, streamlining the visa approval process, and improving decision-making.




# US-Visa-Approval-Prediction

## Pre-requistics

- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- Flowchart: https://whimsical.com/login

  open anaconda Navigator. Select Environments , select the base environment and open the Terminal 
  Go to your US_visa-Approval-Prediction folder in anaconda command prompt

## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n visa python=3.8 -y
```

```bash
conda activate visa
```

```bash
pip install -r requirements.txt
```

```bash
python app.py

### https://www.kaggle.com/datasets/moro23/easyvisa-dataset?resource=download



Create MaongoDB account
MongoDB: https://account.mongodb.com/account/login


Check the url for the orient  parameter  to convert to dictionary in dataset https://www.w3resource.com/pandas/dataframe/dataframe-to_dict.php



## Workflow

1. constant
2. config_entity
3. artifact_entity
4. conponent
5. pipeline
6. app.py / demo.py


- config_entity  input to your entity / flow
- artifact_entity return from your enity/flow

### Export the  environment variable
```bash


export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID = <AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY = <AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION = <AWS_DEFAULT_REGION>

```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.
## 2. Create IAM user for deployment

    #with specific access

	    1. EC2 access : It is virtual machine

	    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

	    1. Build docker image of the source code

	    2. Push your docker image to ECR

	    3. Launch Your EC2 

	    4. Pull Your image from ECR in EC2

	    5. Lauch your docker image in EC2

	  #Policy:

	    1. AmazonEC2ContainerRegistryFullAccess

	    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
    - Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject


## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:


	#optional

	sudo apt-get update -y

	sudo apt-get upgrade -y

	#required

	docker --version

-- download docker to  the  EC2 machine
	curl -fsSL https://get.docker.com -o get-docker.sh

--Install docker in the EC2 ubundu server
	sudo sh get-docker.sh

	docker --version

 -- add docker to sudo group
	sudo usermod -aG docker ubuntu
 -- run docker
	newgrp docker


connect github with aws  EC2 machine EC2 get to kinw how I push  my changes  gitbubso EC2 can

connect github to aws EC2 machine usung self hosted rynenr
# 6. Configure EC2 as self-hosted runner:

Github --> settings--> Actuions--> Runners . Click on New self-hosted runner
    setting>actions>runner>new self hosted runner> choose os> then run command one by one
   select Linux
   Architecture: x64

   copy code from download and execute in  EC2 CLI

# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO	




Notes:

- mongo_db_connection.py  inside configuration folder : create mongodb database connections

- Create data_access folder --> usvisa_data.py:  This class help to export entire mongo db record and return as pandas dataframe


- docker to containerize the application

#### Data Ingestion
- export_data_into_feature_store
- split_data_as_train_test

- initiate_data_ingestion.

ECR
Crteate private repository to store docker image
637734631225.dkr.ecr.us-east-1.amazonaws.com/usvisa

EC2
