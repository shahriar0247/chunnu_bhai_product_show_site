from app import app
from flask import render_template

@app.route("/product/<name>")
def product(name):
    return render_template("product/product.html")