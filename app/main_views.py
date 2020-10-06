from app import app
from flask import render_template, redirect
from app.get_images import get_all_images, get_all_cloths_data, get_tags
import base64

@app.route("/")
def home():
    return redirect("/main")

@app.route("/<tag>")
def main(tag):
    all_images = (get_all_images(tag))
    all_cloths_data = get_all_cloths_data(tag)
    imagelength = len(all_images)
    tags = get_tags()
    tags_length = len(tags)
    main_page = "1"
    return render_template("main/main.html" , main_page=main_page, imagelength=imagelength, all_images=all_images, all_cloths_data=all_cloths_data, tags_length=tags_length, tags=tags)

