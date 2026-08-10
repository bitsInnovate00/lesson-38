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
                        
