from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/submit")
def submit():
    
    w1 = float(request.form['weight1'])
    m1 = float(request.form['mark1'])
    w2 = float(request.form['weight2'])
    m2 = float(request.form['mark2'])

    score = m1 * (w1/100) + m2 * (w2/100)
    
    return render_template("results.html", form_jinja=request.form, score_jinja=score)

if __name__ == "__main__":
    app.run(port=6969)