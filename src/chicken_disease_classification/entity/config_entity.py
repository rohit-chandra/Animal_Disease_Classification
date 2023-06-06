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
    unzip_dir: Path