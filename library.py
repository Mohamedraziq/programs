books=['c++','python','jS','php','flutter','java','css']
while True:
    print('''
          1. borrow book
          2.return book
          3.show all book
          4.exit
          ''')
    choice=int(input("enter the choice: "))
    if choice==1:
        bbook=(input("enter the book to borrow: "))
        if bbook in books:
            books.remove(bbook)
            print("book borrowed successfully")
        else:
            print ("you entered book name not found")
    elif choice==2:
        rbook=input("enter the book nmae to return: ")
        books.append(rbook)
        print("book returned successfully")
    elif choice==3:
        print("available books are...")
        for book in books:
            print(books)
            break
    elif choice==4:
        print("thank you...!!!visit again....!!!")
        break
    else:
        print("please check the option number")