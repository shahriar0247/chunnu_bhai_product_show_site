from app import app
from flask import render_template
from app.get_images import get_all_images, get_all_cloths_data
import base64

@app.route("/")
def main():
   
    all_images = (get_all_images("images"))
    all_cloths_data = get_all_cloths_data()
    length_of_items = len(all_images)
    return render_template("main/main.html" ,length_of_items=length_of_items, all_images=all_images, all_cloths_data=all_cloths_data)