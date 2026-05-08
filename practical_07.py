class ReadingMaterial:
    def __init__(self , title):
        self.title = title 
    
    def display(self):
        return f"Title : {self.title}"

class Book(ReadingMaterial):
    def __init__(self , title, isbn):
        super().__init__(title)
        self.isbn = isbn
    
    def display(self):
        return f"{super().display()} , ISBN: {self.isbn}"
class ReasearchPaper(ReadingMaterial):
    def __init__(self,title,doi):
        super().__init__(title)
        self.doi = doi
        
    def display(self):
        return f"{super().display()} , DOI: {self.doi}"

class Magazine(ReadingMaterial):
    def __init__(self , title , month):
        super().__init__(title)
        self.month = month
    
    def display(self):
        return f"{super().display()} , Month : {self.month}"

def main():
    material = []
    
    while True:
        print("1. Add Book 2. Add Research Paper 3. Add Magazine 4. Display All 5. Exit")
        print("Enter your choice:")
        
        ch = int(input())
        
        if ch == 1:
            title = input("Enter the title of book:")
            isbn = input("Enter the ISBN number of book:")
            material.append(Book(title , isbn))
        elif ch == 2:
            title = input("Enter the title of research paper:")
            doi = input("Enter the DOI number of research paper:")
            material.append(ReasearchPaper(title , doi))
        elif ch == 3:
            title = input("Enter the title of magazine:")
            month = input("Enter the month of magazine:")
            material.append(Magazine(title , month))
        elif ch == 4:
            for item in material:
                print(item.display())
        elif ch == 5:
            print("Program ended")
            break

if __name__ == '__main__':
    main()