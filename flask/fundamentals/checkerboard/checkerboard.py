from flask import Flask, render_template

app = Flask(__name__)

# Have the root route render a template with a checkerboard on it

@app.route('/')
def checkerboard():
    # return render_template("index.html")
    return render_template("index.html",x=8,y=8)

# Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors
@app.route('/<int:x>')
def checkerboard_rows(x):
    return render_template("index.html",x=x, y=8)

# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

@app.route('/<int:x>/<int:y>')
def checkerboard_grid(x,y):
    return render_template("index.html",x=x, y=y)    


if __name__=="__main__":
    app.run(debug = True)