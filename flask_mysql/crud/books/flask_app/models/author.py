from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.books = []

    # Get all authors
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    # Get one author
    @classmethod
    def get_author(cls, data):
        query = "SELECT id, name FROM authors WHERE id = %(id)s;"
        return connectToMySQL("books_schema").query_db(query, data)

    # Save a new author
    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL("books_schema").query_db(query, data)

    # Retrieve list of books favorited by a particular author
    @classmethod
    def get_author_favorites(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE author_id = %(id)s;"
        return connectToMySQL("books_schema").query_db(query, data)

    # Add another book to the author's favorite list
    @classmethod
    def save_favorites(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL("books_schema").query_db(query, data)
