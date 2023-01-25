from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.title = db_data['title']
        self.num_of_pages = db_data['num_of_pages']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.authors = []

    # Get all books
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    # Get one book
    @classmethod
    def get_book(cls, data):
        query = "SELECT id, title FROM books WHERE id = %(id)s;"
        return connectToMySQL("books_schema").query_db(query, data)

    # Save a new book
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)

    # Retrieve list of authors who favorited a particular book
    @classmethod
    def get_book_favorited_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE book_id = %(id)s;"
        return connectToMySQL("books_schema").query_db(query, data)

    # Add another author to the book's favorite list 
    @classmethod
    def save_favorites(cls, data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s);"
        return connectToMySQL("books_schema").query_db(query, data)