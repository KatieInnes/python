from flask import Flask, render_template

app = Flask(__name__)

# Have the /play route render a template with 3 blue boxes

@app.route('/play')
def index():
    return render_template("index.html")

# Have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<int:num>')
def repeat_boxes(num):
    return render_template("repeat_boxes.html",num=num)

# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value

@app.route('/play/<int:num>/<string:color>')
def change_color(num,color):
    return render_template("change_color.html",num=num, color=color)    


if __name__=="__main__":
    app.run(debug = True)