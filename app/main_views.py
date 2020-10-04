from app import app
from flask import render_template
from app.get_images import get_all_images
import base64

@app.route("/")
def main():
   
    all_images = (get_all_images("images"))
    return render_template("main/main.html" , all_images=all_images)