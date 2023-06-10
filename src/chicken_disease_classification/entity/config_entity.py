from dataclasses import dataclass
from pathlib import Path

# this class is a data class and not python class
# the parameters are the return type of the class
# this is similar to data_ingestion present in config.yaml
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path\



@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int



@dataclass(frozen=True)
class CallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    model_checkpoint_dir: Path