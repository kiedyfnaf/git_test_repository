import os
from notebook import notebookapp

# Get the Jupyter installation directory
jupyter_dir = os.path.dirname(notebookapp.__file__)
print(jupyter_dir)