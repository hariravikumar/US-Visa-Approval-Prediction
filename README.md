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

```


- mongo_db_connection.py inside configuration folder : create mongodb database connection

- Create data_access folder --> usvisa_data.py:  This class help to export entire mongo db record and return as pandas dataframe

#### Data Ingestion
- export_data_into_feature_store
- split_data_as_train_test

- initiate_data_ingestion