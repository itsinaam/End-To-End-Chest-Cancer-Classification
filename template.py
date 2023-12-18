import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')



project_name = 'Chest Cancer Clasification'

list_of_files =[
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constant/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'

]


for file_path in list_of_files:
    filepath = Path(file_path)
    file_dir , filename = os.path.split(filepath)

    if file_dir != '':
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating Directory {file_dir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open (filepath,'w') as f:
            pass
            logging.info(f"Empty file is creating {filepath}")


    else:
        logging.info(f"Files {filename} are already created")