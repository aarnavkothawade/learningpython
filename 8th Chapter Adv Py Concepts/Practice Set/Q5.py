class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        print(f"'{self.title}' by {self.author}")

    def __len__(self):
        print(len(self.title))


book1 = Book("The Lost Symbol", "Dan Brown")
book1.__str__()
book1.__len__()