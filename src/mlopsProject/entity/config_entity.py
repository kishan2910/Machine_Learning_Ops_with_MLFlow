from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path   

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path #from config.yaml
    train_data_path: Path #from config.yaml
    test_data_path: Path #from config.yaml
    model_name: str # it will get from params.yaml
    alpha: float # it will get from params.yaml
    l1_ratio: float # it will get from params.yaml
    target_column: str # it will get from schema.yaml 

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path 
    all_params: dict #from params.yaml
    metric_file_name: Path #from config.yaml
    target_column: str #from schema.yaml
    mlflow_uri: str