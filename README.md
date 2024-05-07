# Machine_Learning_Ops_with_MLFlow

## Workflows

1. Update config.yaml # mandatory to store output file of each stage to destination and to store/fetch input of each stage.  
2. Update schema.yaml  # required in model trainer stage to load parameters for model.
3. Update params.yaml # required in model validation stage to match columns and datatypes
4. Update the entity 
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## STEPS:

## STEP 1: Clone the repository
URL: https://github.com/kishan2910/Machine_Learning_Ops_with_MLFlow

## STEP 2: Create and activate virtual environment 
python -m venv mlopsProject
. mlopsProject/scripts/activate

## STEP 3: Install the requirements
pip install -r requirements.txt

## STEP 4: Run the app.py
python app.py

### Dagshub
MLFLOW_TRACKING_URI=https://dagshub.com/kishan2910/Machine_Learning_Ops_with_MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=kishan2910 \
MLFLOW_TRACKING_PASSWORD=b7f010a3c4985624333a1cb0dc113d23f4bed703 \
python script.py

Run this to export as env variables:
export MLFLOW_TRACKING_URI=https://dagshub.com/kishan2910/Machine_Learning_Ops_with_MLFlow.mlflow
export MLFLOW_TRACKING_USERNAME=kishan2910
export MLFLOW_TRACKING_PASSWORD=b7f010a3c4985624333a1cb0dc113d23f4bed703