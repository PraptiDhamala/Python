class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self,name):
        for c in name:
            i=i+1
        return i
    def __call__(self):
        return f"Reading the book {self.title}"

book = Book("Dune", "Frank Herbert")
print(book) 
print(book.title)
print(len(book.title))
print(book())