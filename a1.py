# importing the module
import sys

 # this function will be the first to run as soon as the main function executes
def initial_phonebook():
    rows, cols =int(input("please enter initial numbe of contacts:")), 5

    # we are collecting the initial number of contacts the user wants to have in the
    # phonebook  aldready.user may also enter 0 if he dosent wish to enter any
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" %(i+1))
        print("NOTE: * indicates manndatory fields")

        temp = []
        for j in range(cols):

            if j == 0:
                temp.append(int(input("enter name*:")))
                if temp[j]==''or temp[j]==' ':
                    sys.exit("name is a mandatory field ")
            if j == 1:
                temp.append(int(input("enter number")))
            if j == 2:
                temp.append(str(input("enter email address:")))
                if temp[j]==''or temp[j]==' ':
                    temp[j] =None
            if j == 3:
                temp.append(str(input("enter date of birth:")))
                if temp[j]==''or temp[j]==' ':
                    temp[j] =None
            if j == 4:
                temp.append(str(input("enter category:")))
                if temp[j]==''or temp[j]==' ':
                    temp[j] =None
        phone_book.append(temp)
    print(phone_book)
    return phone_book
                        
def menu():

    print("/t/t/tSMARTPHONE DIRECTORY",flush=False)
    print("/tYou can now perform the following operations on this phone book\n")
    print("1.add a new contact")
    print("2.remove an existing contact")
    print("3.delete all contacts")
    print("4.search for a contact")
    print("5.display all contacts")
    print("6.exit phone book")

    choice=int(input("please enter your choice"))

    return choice

def add_contact (pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("enter name:")))
        if i == 1:
             dip.append(int(input("enter number:")))
        if i == 2:
            dip.append(str(input("enter e-mail address:")))
        if i == 3:
             dip.append(int(input("enter date of birth(dd/mm/yy):")))
        if i == 4:
            dip.append(str(input("enter category(family/friends/work/others):")))
    pb.append (dip)

    return pb

def remove_existing (pb):
    query = str(input("please enter the name of the contact you wish to remove:"))

    temp = 0

    for i in range(len(pb)):
        if query==pb[i][0]:
            temp+=1

            print(pb.pop(i))
            print("this query has now been removed")

            return pb
        if temp == 0 :

            print("Sorry, you have entered an invalid query\n please recheck and try again later.")

            return pb
def delete_all (pb):

    return pb.clear()

def search_existing (pb):
    choice = (int(input("enter search criteria\n\n\n 1.Name\n2.Number\n3.Email-id\n4.DOB\n5.category(family/friends/work/others)\ \nplease Enter:")))

    temp=[]
    check=-1

    if choice ==1:
         query = str(input("please enter the name of the contact you wish to search :"))
    for i in range(len(pb)):
        if query==pb[i][0]:    
           check = i
           temp.append(pb[i])

        elif choice == 3:
            query =str(input("please enter the email id\ of the contact you wish to search:"))
            for i in range(len(pb)):
             check = i
            temp.append(pb[2])

        elif choice == 4:
                    query =str(input("please enter the DOB(dd/mm/yy format ONLY)\ of the contact you wish to search:"))
                    for i in range(len(pb)):
                     check = i
                    temp.append(pb[i])

        elif choice == 5:
                    query =str(input("please enter the contact you wish to search:"))
                    for i in range(len(pb)):
                     check = i
                     temp.append(pb[i])
