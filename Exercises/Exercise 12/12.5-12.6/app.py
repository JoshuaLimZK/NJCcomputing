from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

with open("/Users/joshualim/Developer/NJCcomputing/Exercises/Exercise 12/12.5-12.6/static/products.txt", "r") as f:
    products_list = list(csv.reader(f))

@app.route("/")
def products():
    return render_template("products.html", products=products_list)

@app.route("/product")
def product():
    return render_template("product_frm.html")

@app.post("/add")
def add_product():
    image_file_name = ""
    
    f = open('/Users/joshualim/Developer/NJCcomputing/Exercises/Exercise 12/12.5-12.6/static/products.txt', "a")
    
    if "image" in request.files:
        image_file = request.files["image"]
        image_file_name = image_file.filename

    image_file.save("/Users/joshualim/Developer/NJCcomputing/Exercises/Exercise 12/12.5-12.6/static/images/"+image_file_name)
    
    f.write(f"{request.form['name']},{request.form['description']},{request.form['price']},{image_file_name}")
    
    f.close()
    
    return redirect("/")
    
if __name__ == "__main__":
    app.run(port=6969)