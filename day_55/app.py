from flask import Flask, render_template , request, redirect
import markdown
import os 

app = Flask(__name__)

if not os.path.exists('posts'):
        os.makedirs('posts')

@app.route("/")
def home():
    posts = os.listdir("posts")
    return render_template("home.html", posts=posts)

@app.route("/post/<filename>")
def post(filename):
    with open(f"posts/{filename}", "r", encoding="utf-8") as file:
        content = file.read()
        html_content = markdown.markdown(content)
        return render_template('post.html', content=html_content, title=filename)
    
@app.route("/add-new", methods=["GET", "POST"])
def add_new():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        with open(f"posts/{title}", "w", encoding="utf-8") as file:
            file.write(content)
        return redirect("/")    
    return render_template("add_new.html")

if __name__ == "__main__":
    app.run(debug=True)
