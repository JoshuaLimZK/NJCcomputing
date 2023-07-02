from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def calculate():
    output = "Hello Worlds"
    return output

if __name__ == "__main__":
    app.run(debug = False)