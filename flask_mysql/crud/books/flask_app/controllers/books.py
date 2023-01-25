from flask import render_template, redirect, request 
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author

# Call Book get_all method to display all books in database
@app.route('/books')
def all_books():
    books = Book.get_all()
    return render_template("books.html", books=books)

# Respond to POST request on route, call the Book model's save method in order to add the new book to the database. 
# Redirect to the books page, now showing the newly added book.
@app.route('/book/create', methods=["POST"])
def create_book():
    Book.save(request.form)
    return redirect('/books')

# Using the id of the selected book, display the authors who have listed it as their favorite.
@app.route('/books/<int:id>')
def books(id):
    data = {
        "id": id
    }
    return render_template("book_show.html", book=Book.get_book(data)[0], favorites=Book.get_book_favorited_authors(data), authors=Author.get_all())

# Respond to POST request on route, call on the add_book_favorite method on the Book model so as to add a new author to the book's list.
# Redirect to selected book's page, now showing the newly added author.
@app.route('/books/<int:id>/add', methods=["POST"])
def add_book_favorite(id):
    Book.save_favorites(request.form)
    return redirect('/books/' + str(id))