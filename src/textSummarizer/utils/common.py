import os
#from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import os


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """_summary_

    Args:
        path_to_yaml (Path): _description_

    Raises:
        ValueError: _description_
        e: _description_

    Returns:
        ConfigBox: _description_
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Read yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    #except BoxValueError:
        # raise ValueError('yaml file is empty or not in correct format') 
    except Exception as e:
        raise e   
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create a list of directories

    Args:
        path_to_directory (Path): list of path directories
        ignore_if_exists (bool, optional): ignore if multiple directories are created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at {path}")
    
@ensure_annotations
def get_size(file_path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"

    