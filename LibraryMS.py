

class Library:
    def __init__(self, books_names):
        self.lstbook=books_names
        self.books=[]
        self.copies=[]
        
    def pos(self, name):
        for i,naame in enumerate(self.lstbook):
            if name in naame:
                return i
    
    def list_all_books(self):
        print(f'{len(self.lstbook)} books are available:')
        count=1
        for name in self.lstbook:
            print(count,'\b.' , name[0].title()) 
            count+=1
        print('')
    
    def available_books(self):
        for i in self.books:
            print(i)
    
    
    def searchbyfield(self, str, field):
        for index,name in enumerate(self.lstbook):
            if (field+1)<=len(name):
                if str == self.lstbook[index][field]:
                    print(self.lstbook[index])

    def check(self, name):
        for nam in checkout:
            for key,item in nam.items():
                if key == name:
                    return item
   
    def borrowBook(self, name, bookname):
        if Library.check(self, name) == 0:
            print("YOU CAN'T CHECK-OUT MORE THAN 5 BOOKS")
        if self.copies[Library.pos(self,bookname)] == 0:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            if name not in track_name:
                track.append({name: [bookname]})
            # print(track)
            
            for i in track:
                if name in track_name:
                    for value, item in i.items():
                        item.append(f'{bookname}')
                        break
                    
                new=5-len(i.get(f'{name}'))
                print(new)   
                checkout.append({name: new})
                print(checkout)
                break
            
            self.copies[Library.pos(self, bookname)]-=1
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN BEFORE 10 DAYS.\n")
            if self.copies[Library.pos(self, bookname)] == 0:
                self.books.remove(bookname)
            track_name.add(name)

    
    def returnBook(self, bookname):
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)
                    
    

                   
        
        
class Member:
    
    def __init__(self, barcode='#'):
        pass
        
    def names(self):
        self.name=input('Enter your name here: ')
        return self.name
        
           
    def requestBook(self):
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book
    
    def check_out(self):
        print("So, you want to check-out a book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
    
    def how_many_days(self):
        print('You can borrow for maximum 10 days')
        dayi=int(input('Borrowing for how may days? '))
        # if dayi >10;
            
            


if __name__ == "__main__":  
      
    # lib.books is variable shows current values, : available_book
    field =['title','author','subject','published date','rack', 'unique_id number', 'copies']  
    # print(len(field))
    print('Welcome to the Library:')

    lib=Library([
        ['father of god','.','.','.','.'], 
        ['the lost world','Canon Doyle', 'adventure', '29 Aug 1995', 'Lib-A 2,30'], 
        ['half girlfriend','.','.','.','.','2'], 
        ['sherlock holmes','canon doyle','mystery','.','.' ], 
        ['ignited minds', 'APJ Abdul Kalam', 'motivation', '11 March 2012', 'Lib-D 4,13', '3'],
        ['a','.','.','.','.'],
        ['b','.','.','.','.'],
        ['c','.','.','.','.'],
        ['d','.','.','.','.'],
        ['e','.','.','.','.'],
        ['f','.','.','.','.']
        ])

    member=Member()
    track = []
    checkout = []
    track_name= set()
    # mem1=Member('Hardik Sharma')
    # mem2=Member('Rajesh Kumar')

    for index,name in enumerate(lib.lstbook):
        name.insert(5,f'{index+1}')                     #unique_id

    for index,name in enumerate(lib.lstbook):
        if len(name)==6:
            name.insert(6,'1')                          #copies
            

    for name in lib.lstbook:
        lib.books.append(name[0])        #book
      
        
    for name in lib.lstbook:
        lib.copies.append(int(name[6]))        #copies_var
           




    # print(lib.lstbook)
    # print(lib.books)
    # print(lib.copies)
    # print(mem1.name)
    # print(member.name)
    # print(mem2.name)
    # exit()

    # print(lib.lstbook[0].title())
    # lib.list_all_books()



    while (True):
        # print(track)
        try:
            print('\nChoose an action to continue:')
            print("""
                  No.   Actions
                  1     List all books
                  2     List all available books
                  3     Search a book     
                  4     Check-Out a book
                  5     Return book
                  6     Track
                  7     Exit the library
                  """)

            action = int(input('Enter you choice: '))

            if action == 1:
                lib.list_all_books()
                
            elif action == 2:
                lib.available_books()
                
            elif action == 3:
                print('Choose any Field:')
                print('')
                for index,name in enumerate(field, start=1):
                    print(index, name)
                print('')

                ask=int(input('enter field index: '))

                for num in range(len(field)):
                    # print(num)    
                    if ask==num+1:
                        str=input('Enter what {}: '.format(field[num]))
                        lib.searchbyfield(str,ask-1)
                        
            elif action == 4:  # borrow or check-out
                lib.borrowBook( 
                    member.names(), member.requestBook())
                
            elif action == 5:  # return
                lib.returnBook(member.returnBook())   
                    
            elif action == 6:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"'{', '.join(book)}' books are taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
                    
            elif action == 7: #exit
                print(track)
                print("THANK YOU ! \n")
                exit()
            else:
                        print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print(f"{e}---> INVALID INPUT! \n")                
                        
                        
                                        