from flask import render_template, redirect, request 
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

# index page is empty, immediately redirects to the authors page
@app.route('/')
def index():
    return redirect('/authors')  

# Call Author get_all method to display all authors in database
@app.route('/authors')
def all_authors():
    authors = Author.get_all()
    return render_template("authors.html", authors=authors)

# Respond to POST request on route, call the save method on the Author model so as to add the new author to the database.
# Redirect to authors page, now showing the newly added author.
@app.route('/author/create', methods=["POST"])
def create_author():
    Author.save(request.form)
    return redirect('/authors')

# Using the id of the selected author, display their favorite books. 
@app.route('/authors/<int:id>')
def authors(id):
    data = {
        "id": id
    }
    return render_template("author_show.html", author=Author.get_author(data)[0], favorites=Author.get_author_favorites(data), books=Book.get_all())

# Respond to POST request on route, call on the save_favorites method on the Author model so as to add a new favorite book to the author's favorites.
# Redirect to selected author's page, now showing the newly added favorite book.
@app.route('/author/<int:id>/add', methods=["POST"])
def add_author_favorite(id):
    Author.save_favorites(request.form)
    return redirect('/authors/' + str(id))
