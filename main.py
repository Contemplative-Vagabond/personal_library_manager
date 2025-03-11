
#class for library
class Library:
    def __init__(self, path_to_file):
        self.inventory = ""
        with open(path_to_file) as f:
            text = f.read
            index = 0
            for line in text.split():
                self.inventory[index] = line
                index += 1


class Shelf(Library):
    def __init__(self):
        super().__init__()

#class for book
class Book:
    def __init__(self):
        pass

    #function for adding book to library
    def add_book():
        pass 

path = "library/inventory.csv"
lib = Library(path)
print(lib.inventory)

print("your books here...")