from flask import Flask, render_template, request, redirect

from user import User
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')  

@app.route('/users')
def user_table():
    users = User.get_all()
    print(users)
    return render_template("index.html", users=users)

@app.route('/users/new')
def new_user():
    return render_template("new_users.html")

@app.route('/create', methods=["POST"])
def create_user():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }

    id = User.save(data)
    return redirect('/users/' + str(id))

@app.route('/users/<int:id>')
def user_info(id):
    data = {
        "id": id
    }
    return render_template("users_read.html", user=User.user_view(data))

@app.route('/users/<int:id>/edit')
def edit_users(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=User.user_view(data))

@app.route('/users/update', methods=["POST"])
def update():
    data = {
        "id" : request.form["id"],
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.edit(data)
    return redirect('/users/' + request.form["id"])

@app.route('/users/<int:id>/delete')
def delete(id):
    data = {
        "id": id
    }

    User.delete(data)
    return redirect('/users')  


if __name__ == "__main__":
    app.run(debug=True) 