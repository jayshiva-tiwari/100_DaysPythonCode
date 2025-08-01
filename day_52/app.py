from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Flask World! 🚀</h1>"

@app.route("/about")
def about():
    return "<h1 style='color:green; text-align:center; font-size:50px' > About my self, John Doe 👋</h1>"

if __name__ == "__shiva__":
    app.run(debug=True)
