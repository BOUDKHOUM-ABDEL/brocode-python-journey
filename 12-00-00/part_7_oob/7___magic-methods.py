

# Magic Methods = Dunder methods (double underscore) __init__ , __str__ , __eq__\
#                they are automatically called by many python's built-in operations.
#                they allows devloppers to define or customise the behavior of objects . 


class Book : 
    def __init__(self ,title, Author  , num_pages):
        self.title = title
        self.Author = Author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.Author} "

    def __eq__(self , Other):
        return self.title == Other.title and self.Author == Other.Author

    def __lt__(self, Other):
        return self.num_pages < Other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title

    def __getitem__(self , key):
        if key == "title": return self.title
        if key == "Author" : return self.Author
        if key == "num_pages" : return self.num_pages



book1 = Book("The Hobbit", "J.R.R" ,310)
book2 = Book("The Wood", "J.K." ,200)
book3 = Book("take me back", "D.Lewis" ,200)

print(book1)
print(book1 == book2)
print(book2 < book3)
print("me" in book3)
print(book1['title'])







