__all__ = [ 'project_path']


import os
import sys
import flask

project_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, project_path)

from random import choice


from app_setting import app
from views import  *
from models import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
