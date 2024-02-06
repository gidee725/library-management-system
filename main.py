class Library:
    def __init_(self):
        self.books_store = []

    def add_book (self, book):
        self.books_Store.append(book)
        return self.books_store

    def remove_book (self, book):
        return self.books_store.pop(book)
    
    def update_book (self,book):
        index = self.books_store(book)
        self.books_store[index]  = book
        return self.books_store
        
    
    
class Book:
    def __init_(self, IBN, title, author,genre, availability):
        self.IBN = IBN
        self.title = title
        self.author = author
        self.genre = genre
        self.avaiability = availability

