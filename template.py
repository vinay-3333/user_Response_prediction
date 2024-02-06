import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

package_name= "User_Response_Prediction"


list_of_files=[
   ".github/workflows/.gitkeep",
   f"{package_name}/__init__.py",
   f"{package_name}/notebook/__init__.py",
   f"{package_name}/notebook/data",
   f"{package_name}/notebook/EDA.ipynb",
   f"{package_name}/notebook/Model_training.ipynb",
   f"{package_name}/src/components/__init__.py",
   f"{package_name}/src/components/data_ingestion.py",
   f"{package_name}/src/components/data_transformation.py",
   f"{package_name}/src/components/model_trainer.py",
   f"{package_name}/src/pipeline/__init__.py",
   f"{package_name}/src/pipeline/prediction_pipeline.py",
   f"{package_name}/src/pipeline/training_pipeline.py",
   f"{package_name}/src/__init__.py",
   f"{package_name}/src/exception.py",
   f"{package_name}/src/logger.py",
   f"{package_name}/src/utils.py", 
   f"{package_name}/README.md",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "params.yaml",
   "requirements.txt", 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "app.py" 
                ]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
        