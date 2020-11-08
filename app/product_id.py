from werkzeug.exceptions import MethodNotAllowed
from app import app
from flask import render_template, request
import os
import random
from app.get_images import get_new_image_id
import sqlite3

UPLOAD_FOLDER = os.path.join(os.getcwd(), "images")
ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg', ".heif", ".heic"]

def allowed_file(filename):
    for extension in ALLOWED_EXTENSIONS:
        if filename.lower().endswith(extension):
            return True
    return False

def image_upload_directory():
    os.getcwd()

def save_image(image_id, image):
    save_path =UPLOAD_FOLDER
    try:
        os.mkdir(UPLOAD_FOLDER)
    except:
        pass
    try:
        os.mkdir(save_path)
    except:
        pass
    save_name = os.path.join(save_path, str(image_id))
    image.save(save_name)

def save_to_db(image_id, price, tag):
    with sqlite3.connect("database/cloths_db") as conn:
        conn.cursor().execute("insert into cloth values (?,?,?)", [image_id, price, tag])

@app.route("/setid", methods = ["POST", "GET"])
def setid():

    if request.method == "POST":
        price =  request.form["price"]
        tag = request.form["tag"]
        if request.files:
            image = request.files["image"]
            print(image.filename)
            if allowed_file(image.filename):
                if not price == "":

                    image_id = get_new_image_id()
                    save_image(image_id, image)
                    save_to_db(image_id,price, tag)

                else:
                    return "Price in empty"
            else:
                return "File type not allowed"
        else:
            return "No file given"
            
    
    return render_template("product_id/setid.html")