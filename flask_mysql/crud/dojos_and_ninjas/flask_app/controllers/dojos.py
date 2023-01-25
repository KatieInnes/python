from flask import render_template, redirect, request 
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')  

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route('/create/dojo', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojos/<int:id>')
def dojo_ninjas(id):
    data = {
        "id": id
    }
    return render_template("dojo_show.html", dojo=Dojo.get_dojo_with_ninjas(data))