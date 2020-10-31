from flask import Flask


app = Flask(__name__)

from app import main_views

from app import product_id
from app import product