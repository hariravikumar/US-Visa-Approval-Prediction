from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 

@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str   

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str    


@dataclass
class ClassificationMetricArtifact:
    accuracy:float
    f1_score:float
    precision_score:float
    recall_score:float


@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str         # for Model path
    metric_artifact:ClassificationMetricArtifact    #for Classification Metric f1 score,precision,recall


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool      # is model accepted to push to S3
    changed_accuracy:float      # how much accuracy changed  between S3 and trained model 
    s3_model_path:str           # S3 model path
    trained_model_path:str      # trained  model path


@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str    