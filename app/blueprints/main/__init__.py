from flask import Blueprint
import os

main = Blueprint('main', __name__,template_folder='templates',static_folder='static')

from . import routes