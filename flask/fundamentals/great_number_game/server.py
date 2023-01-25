from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

import random

@app.route('/')
def index():
    if "num" not in session:
        session["num"] = random.randint(1, 100)
    return render_template("index.html")


@app.route('/guess', methods=["POST"])
def guess():
    session["guess"] = int(request.form["guess"])
    return redirect('/')

@app.route('/start_again')
def start_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
