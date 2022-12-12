#class BookStore
#inst var Name and Author cls var NoOfBooks=0 cls method dispaly all
#initialise instance

class BookStore:
    NoOfBooks=0
    def __init__(self):
        self.Name="qwe"
        self.Author="asdf"
        BookStore.NoOfBooks=BookStore.NoOfBooks+1

    def Accept(self):
        print("Enter the book name:")
        self.Name=input()

        print("Enter the author name:")
        self.Author=input()
    
    def Display(self):
        
        
        print("Book Name:",self.Name)
        print("Author Name:",self.Author)


def main():
    obj=BookStore()
    obj.Accept()
    
    print("No of Book:",BookStore.NoOfBooks)
    obj.Display()
    obj1=BookStore()
    obj1.Accept()
    print("No of Book:",BookStore.NoOfBooks)
    
    
   
   
    obj1.Display()




if __name__ == "__main__":
    main()