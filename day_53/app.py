from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home ():
    return render_template("index.html", name = "shiva")

@app.route("/about")
def about():
    return render_template("about.html", name = "tiwari")

if __name__ == "__main__":
    app.run(debug=True)

