import yaml
from housing.exception import HousingException 
import os,sys 

# Any Helper functions we write in util file 
# The functionality which are not the part of main file but required during pipeline in multiple places as a help 
def read_yaml_file(file_path:str)->dict:
    """ 
    Read a YAML file and return the contents as a dictionary . 
    file_path : str 
    
    """
    try : 
         
        with open(file_path, "rb") as yaml_file : 
            return yaml.safe_load(yaml_file)
    except Exception as e : 
        raise HousingException(e,sys) from e 