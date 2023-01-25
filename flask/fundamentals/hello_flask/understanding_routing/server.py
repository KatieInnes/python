


from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# localhost:5000/ - have it say "Hello World!"
@app.route('/')
def hello_world():
    return 'Hello World!'

# localhost:5000/dojo - have it say "Dojo!"
@app.route('/')
def dojo():
    return 'Dojo!'

# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def greeting(name):
    print(name)
    return f"Hi {name}!"

# Create one url pattern and function that can handle the following examples (HINT: path variables are by default passed as strings. How might you handle a number?):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{word * num}"


if __name__=="__main__":
    app.run(debug = True)

# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, they receive an error message saying "Sorry! No response. Try again."