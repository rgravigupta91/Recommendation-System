import os, sys
from pathlib import Path
import logging

while True:
    Project_name = input("Enter Project Name: ")
    if Project_name!= '':
        break
while True:
    jupyter = input('Enter the jupyter file name: ')
    if jupyter != '':
        break

list_of_files = [
    # Write your folder names as per your projects and run the code

    # f'{Project_name}/__init__.py',
    # f'{Project_name}/components/__init__.py',
    # f'{Project_name}/config/__init__.py',
    # f'{Project_name}/constants/__init__.py',
    # f'{Project_name}/entity/__init__.py',
    # f'{Project_name}/exception/__init__.py',
    # f'{Project_name}/logger/__init__.py',
    # f'{Project_name}/pipeline/__init__.py',
    # f'{Project_name}/utils/__init__.py',
    # f'{Project_name}/Jupyter_notebook/{jupyter}.ipynb',
    # f'config/config.yaml',
    # 'schema.ymal',
    # 'app.py',
    # 'main.py',
    # 'logs.py',
    # 'exceptions.py',
    # 'setup.py'

    'requirements.txt' 
]

list_of_folders = [
    'data/',
    'models/',
    'notebooks/',
    'api/',
    'frontend/',
    'utils/',
     
]


for folder in list_of_folders:
    os.makedirs(folder, exist_ok=True)


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass

    else:
        logging.info("file is already present")


        