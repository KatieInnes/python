from flask import render_template, redirect, request 
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def new_ninja():
    return render_template("new_ninja.html", dojos=Dojo.get_all())

@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')

@app.route('/ninjas/<int:id>')
def ninja_info(id):
    data = {
        "id": id
    }
    return render_template("ninjas_read.html", ninja=Ninja.ninja_view(data))

@app.route('/ninjas/<int:id>/edit')
def edit_ninjas(id):
    data = {
        "id": id
    }
    return render_template("edit_ninja.html", ninja=Ninja.ninja_view(data))

@app.route('/ninjas/update', methods=["POST"])
def update():
    data = {
        "id" : request.form["ninjas.id"],
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"]
    }
    Ninja.edit(data)
    return redirect('/ninjas/' + request.form["id"])

@app.route('/ninjas/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }

    Ninja.delete(data)
    return redirect('/ninjas')