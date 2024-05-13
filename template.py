import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files =[
    ".github/wrokflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    
]