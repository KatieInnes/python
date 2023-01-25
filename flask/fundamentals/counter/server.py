from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# our index route will handle rendering our form
@app.route("/")
def index():
    if "view" not in session:
        session["view"] = 0
    else:
        session["view"] += 1   
    return render_template("index.html") 

# localhost:5000/destroy_session - Clear the session. Once cleared, redirect to the root.
@app.route("/destroy_session")
def clear():
    session.clear()
    return redirect("/")


# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route("/two_visits")
def two_visits():
    session["view"] += 1
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)