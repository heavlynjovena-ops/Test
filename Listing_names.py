import os

name = []

while True:
    os.system('clear')
    choice = int(input("Menu:\n1. View list\n2. Add name in list\n3. Edit name in list\n4. Delete name from list\n5. Exit Menu\nEnter option number (1-5): "))
    if choice == 5:
        input('press enter')
        break
    elif choice == 2:
       while True:
        os.system('clear')
        name2 = input('Enter name: ')
        name.append(name2)
        again = input('Add new name? (y/n): ')
        if again == "n":
            break
    elif choice == 1:
        if len(name) > 0:
           num = 1
           for s in name:
              print(f"{num}.{s}")
              num += 1
        else:
           print("No names entered.")
    elif choice == 3:
        if len(name) == 0:
          print("No names entered.")
        else: 
            num = 1
            for s in name:
              print(f"{num}.{s}")
              num += 1
            choice2 = int(input("Enter student number to edit: "))
            name3 = input("Enter new name: ")
            name[choice-1] = name3
            print("Student name has been edited!")
    elif choice == 4:
        if len(name) == 0:
            print("No names entered.")
        else:
            num = 1
            for s in name:
                print(f"{num}.{s}")
                num += 1
            choice3 = int(input("Enter student number to delete: "))
            del name[choice3-1]
            print("Student name has been deleted!")
    input("Press enter to continue!")