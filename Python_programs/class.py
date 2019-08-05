class Book:
    def __init__(sd,title,authors,publishers,isbn,price):
        sd.title=title
        sd.authors=authors[:]
        sd.publishers=publishers
        sd.isbn=isbn
        sd.price=price
    def uthors(self):
        return len(self.authors)
python=Book('qwerty',['gupta','hello'],'grb',120987654,2345.45)
print(python.price)
print(python.uthors())
