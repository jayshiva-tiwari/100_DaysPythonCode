from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def feedback_form():
    return render_template('form.html')

@app.route("/submit", methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']
    # Here you would typically save the feedback to a database or send it via email
    return render_template('thankyou.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)