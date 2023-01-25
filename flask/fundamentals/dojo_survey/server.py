from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


# Have the root route ("/") display a nice looking HTML form.  
@app.route('/')
def index():
    return render_template("index.html")

# The form should be submitted to '/process'
@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['soda'] = request.form['soda']
    session['comment'] = request.form['comment']
    return redirect('/result')

# http://localhost:5000/result - have this display a html with the information that was submitted by POST. Have the "/result" route display the information from the form on a new HTML page
@app.route('/result')
def user_info():
    return render_template('result.html', name_on_template=session['name'], location_on_template=session['location'],language_on_template=session['language'],
    soda_on_template=session['soda'],comment_on_template=session['comment'])

if __name__ == "__main__":
    app.run(debug=True)