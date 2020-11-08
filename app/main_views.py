from app import app
from flask import render_template, redirect
from app.get_images import get_all_images, get_all_cloths_data, get_tags
import base64

@app.route("/")
def home():
    return redirect("/main")

@app.route("/<tag>")
def main(tag):
    all_cloths_data = get_all_cloths_data(tag)
    imagelength = len(all_cloths_data)
    tags = get_tags()
    tags_length = len(tags)
   
    return render_template("main/main.html" ,  imagelength=imagelength, all_cloths_data=all_cloths_data, tags_length=tags_length, tags=tags)

def get_data(tag):
    all_cloths_data = get_all_cloths_data(tag)
    imagelength = len(all_cloths_data)
    return all_cloths_data, imagelength

@app.route("/main2")
def main2():
    main = get_data("main")
    panjabi = get_data("panjabi")
    shirt = get_data("shirt")
    t_shirt = get_data("t-shirt")
    return render_template("main2/main2.html" ,  main=main, panjabi=panjabi, shirt=shirt, t_shirt=t_shirt)

