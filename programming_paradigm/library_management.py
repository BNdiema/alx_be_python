class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False



class Library:
    def __init__(self):
        self._book = []

    def add_book(self, title, author):
        book = Book(title, author)
        self._book.append(book)

    def check_out_book(self, title):
        if title in self._book:
            self._book.remove(title)

    def return_book(self, title):
        for book in self._book:
            if book.title == title:
                return f"You have returned {title}."
            else:
                return f"{title} was not check out"

    def list_available_books(self):
        print(self._book)