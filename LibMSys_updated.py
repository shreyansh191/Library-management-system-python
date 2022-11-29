
class Library:
    def __init__(self, books_names):
        self.lstbook=books_names
        self.books=set()
        self.copies=[]
        self.date=1
            
    def pos(self, bookname):
        for i,naame in enumerate(self.lstbook):
            if bookname in naame:
                return i
    
    def list_all_books(self):
        print(f'{len(self.lstbook)} books are available:')
        count=1
        for name in self.lstbook:
            print(count,'\b.' , name[0]) 
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
            for key,value in nam.items():
                if key == name:
                    return value
        return 1
    
    def atfter_resv(self, name, bookname):
        if name in resvtrack:
            for lst in resvtrack[name]:
                if lst[0] == self.pos(bookname):
                    lst[1]-=1
                    if lst[1]==0:
                        resvtrack.pop(name)
                    return True
        return False        
        
        
    def borrowBook(self, name, bookname):
        if Library.check(self, name) == 0:
            print("YOU CAN'T CHECK-OUT MORE THAN 5 BOOKS")
        elif self.atfter_resv(name, bookname):
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN BEFORE 10 DAYS.\n")
        elif self.copies[Library.pos(self,bookname)] == 0:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN OR RESERVED BY SOMEONE ELSE, WAIT UNTIL AVAILABILITY\n")
            resv=input("Do you wanna reserve this book?(y/n): ")
            if resv=='y':
                self.reserve(name,bookname)
        else:
            if name not in track_name:
                track.append({name: [bookname]})
                
            if bookname not in track_bybook:
                track_bybook[bookname]={name}
            else:
                track_bybook[bookname].add(name)
            
            new=0
            for i in track:
                if name in track_name:
                    for key, value in i.items():
                        value.append(f'{bookname}')
                if i.get(f'{name}') != None:
                    new=5-len(i.get(f'{name}'))
                
             
            if name not in track_name:  
                checkout.append({name: new})
            else:
                for name1 in checkout:
                    name1[name]=new
                    break
            
            self.date_tr_add(name, bookname)
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN BEFORE 10 DAYS.\n")
            print(f"BARCODE OF BOOK:'{self.booktobar(bookname)}'")
            self.copies[Library.pos(self, bookname)]-=1         #how many copies are available for a particular book
            if self.copies[Library.pos(self, bookname)] == 0:
                self.books.remove(bookname)
            track_name.append(name)
            

    def returnBook(self, bookname):
        posn=self.pos(bookname)
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.add(bookname)
        self.copies[posn]+=1
        for key,value in resvtrack.items():
            if value[0]==posn:
                self.copies[posn]-=1   
                break
        
       
    def date_tr_add(self, name, bookname):
        date_tr[(name,self.booktobar(bookname))] = self.date
        

    def add_book(self,title,author='.',subject='.' ,published_date='.',rack='.', copies='.'):
        self.lstbook.append([f'{title}',f'{author}',f'{subject}',f'{published_date}',f'{rack}', f'{copies}'])
        last=len(self.lstbook)-1
        self.lstbook[last].insert(5,f'{last}') #unique_id
        if self.lstbook[last][6]=='.':
            self.lstbook[last][6]='1'          #copies
        print(lib.lstbook)
       
    def reserve(self, name, bookname):
        print('So, you want to reserve books!')
        copies_book=int(self.lstbook[self.pos(bookname)][6])
        copies_ask=1
        sum=0
        for key, value in resvtrack.items():
            for lst in value:
                if lst[0] == self.pos(bookname):
                    sum+=lst[1]
        print('sum =',sum)
        print('copies_book =',copies_book)
        
        if sum == copies_book:
            print("All items of {} are already reserved so you can't reserve the book for now".format(bookname))
            return None
        
        if sum == 0:
            resv_cop_aval=copies_book
        else:
            resv_cop_aval=sum
            
        if copies_book != 1:
            print(f"There are {copies_book} items for {bookname}")
            copies_ask=int(input('How many items (if) do you wanna reserve\n(only {} copies available): '.format(resv_cop_aval)))     
            
        if name not in resvtrack:
            resvtrack[name] = [[Library.pos(self, bookname),copies_ask]]
            print('Thankyou')
            print(f'{bookname} has been reserved for you!')
        else: 
            if resvtrack[name][0] == self.pos(bookname):
                resvtrack[name][1]+=1
            else:
                resvtrack[name].append([Library.pos(self, bookname),copies_ask])
                
            print('Thankyou')
            print(f'{bookname} has been reserved for you!')
            return None
    
    def booktobar(self, bookname):
        return f"{self.pos(bookname)}b{self.copies[self.pos(bookname)]}"
    
    def bartobook(self, bar):
        i_b=bar.find('b')
        bookname=self.lstbook[bar[:i_b]-1]
        bookitem=bar[bar[i_b+1:]]
        return bookname

            
        
            
            
                            
class Member:
    
    def __init__(self):
        pass
        
    def names(self):
        self.name=input('Enter your name here: ')
        return self.name
        
           
    def requestBook(self,name):
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ")
        ask=input('Enter Member id barcode:')
        bar_mtr[ask]=name
        return self.book

    def returnBook(self):
        print("So, you want to return book!")
        ask=input('Enter Member id barcode or your Name:')
        if ask in bar_mtr:
            name=bar_mtr[ask]
            print(f"Hy, {name}!")
        else:
            name = ask
            self.book = input("Enter name of the book you want to return: ")
        
        count=0
        print('Options for Book-Barcode:')
        for key in date_tr:
            if name in key:
                count+=1
                print(f"{count}. '{key[1]}' checked out on date {date_tr[key]}")
                
        bar_input=int(input('Choose barcode of the book(ENTER Sr.No): '))
        
        count=0
        for key in date_tr:
            if name in key:
                count+=1
                if count==bar_input:
                    bar_in=key[1]
                    break
        
        if lib.date - date_tr[(name,bar_in)]+1 >10:
            print('')
            print('The book is NOT returned within 10 days')
            print('Taking care of our policies, you are charged with an amount of Rs.50')
            print("Rs50 has been deducted from you library membership card.")
          
        for i in track:
            if name in track_name:
                for key, value in i.items():
                    value.remove(f'{self.book}')
        
        track_name.remove(name)
        
        if name not in track_name:
            track.remove({name: []})
            for lst in checkout:
                checkout.remove({name: lst[name]})
                
        
        
        for name1 in checkout:
            name1[name]+=1
            break
        
        for i in track:
            if self.book not in i[name]:
                track_bybook[self.book].remove(name)
        if track_bybook[self.book] == set():
            track_bybook.pop(self.book)
            
        
            
        return self.book
            
            


if __name__ == "__main__":  
      
    # lib.books is variable shows current values, : available_book
    field =['title','author','subject','published date','rack', 'unique_id number', 'copies']  
    
    print('Welcome to the Library:')

    lib=Library([
        ['godfather','mario','fiction','1969','1'], 
        ['the lost world','arthur conan doyle', 'adventure', '1995', 'lib a block 2'], 
        ['half girlfriend','chetan bhagat','romance','2014','lib a block 1','2'], 
        ['sherlock holmes','arthur conan doyle','mystery','1892','lib e block 1' ], 
        ['ignited minds', 'apj abdul kalam', 'motivation', '2012', 'lib d block 4', '3'],
        ['verity', 'coolen', 'mystery', '2020' , 'lib c block 3', '5'],
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
    track_name=[]
    resvtrack= {}
    track_bybook={}
    date_tr={}
    bar_mtr={}

    for index,name in enumerate(lib.lstbook):
        name.insert(5,f'{index+1}')                     #unique_id

    for index,name in enumerate(lib.lstbook):
        if len(name)==6:
            name.insert(6,'1')                          #copies
            

    for name in lib.lstbook:
        lib.books.add(name[0])        #book
      
        
    for name in lib.lstbook:
        lib.copies.append(int(name[6]))        #copies_var



    while (True):
        
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
                  8     Developer
                  9     Change Date
                  """)

            action = int(input('Enter you choice: '))

            if action == 1:
                lib.list_all_books()
                
            elif action == 2:
                lib.available_books()
                
            elif action == 3:   #Search
                print('Choose any Field:')
                print('')
                for index,name in enumerate(field, start=1):
                    print(index, name)
                print('')

                ask=int(input('enter field index: '))

                for num in range(len(field)):
                      
                    if ask==num+1:
                        str=input('Enter what {}: '.format(field[num]))
                        lib.searchbyfield(str,ask-1)
                        
            elif action == 4:  # borrow or check-out
                mem_name=member.names()
                lib.borrowBook( 
                    mem_name, member.requestBook(mem_name))
                
            elif action == 5:  # return
                lib.returnBook(member.returnBook())   
                    
            elif action == 6:  # track
                print(track)
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = set()
                        for lst in value:
                            book.add(lst)
                        print(f"'{', '.join(book)}' book/s is/are check-out by {holder}.")
                print("\n")
                
                for key,value in track_bybook.items():
                    book=key
                    holder=value
                    print(f"'{book}' book is check-out by '{', '.join(holder)}'")
                    
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
                    
            elif action == 7: #exit
                print("THANK YOU ! \n")
                exit()
            
            elif action == 8:   #developer
                
                print('lib.books:\n',lib.books)
                print('track:\n',track)
                print('lib.copies:\n',lib.copies) 
                print('track_name:\n',track_name)  
                print('checkout:\n',checkout)               #checkout times of a particular member
                print('resvtrack:\n',resvtrack)
                print('track_bybook:\n',track_bybook)
                print('lib.date_tr:\n',date_tr)
                print('date:\n',lib.date)
                print('bar_mtr:\n',bar_mtr)
                
                                 
                # print('lib.lstbook:\n',lib.lstbook)
            
            elif action == 9:   #date jump 
                dt=int(input(f"Enter the date to jump on\n (which should be greater than or equal to the current date= '{lib.date}')\n: "))
                if dt >=lib.date:
                    lib.date=dt
                else:
                    print('ERROR, please retry:')
                    
            elif action == 10:  #add book to library
                lib.add_book(input('Enter book name: '))   
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print(f"{e}---> INVALID INPUT! \n")                
                    
