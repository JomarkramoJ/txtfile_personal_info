with open("./information_list.py", "a") as file_handle:

    informations = {}

    def is_valid_name(input_string):
        if any(char.isdigit() for char in input_string):
            return False
        return True

    while True:
        while True:    
            name = input("Please enter your full name: ")
            if is_valid_name(name):
                break
            else:
                print("Name cannot contain numbers. ")
        while True:
            try:
                age = int(input("Enter age: "))
                if age >= 123 and age <= 130:
                    print("You now have the world record of being the oldest ever to live according to google")
                    break
                elif age >= 0 and age <= 130:
                    break
                else:
                    print("invalid age")
            except:
                print("Enter a valid age ")
        while True:
            address = input("Enter your address: ")
            break
        for i in range(6):
            birthday = input("Enter your birthday (MMDDYYYY): ")
            if len(birthday) == 8 and birthday.isdigit():
                formatted_birthday = f"{birthday[:2]},{birthday[2:4]},{birthday[4:]}"
                print(f"Formatted birthday: {formatted_birthday}")
                break
            else:
                print("Please follow this format MMDDYYYY:")



    # file_handle.write("Name: " + input("Enter Name: \n") + "\n")
    
    
    
    # while True:
    #     try:
    #         age = str(int(input("Enter Age: ")))
    #         file_handle.write("Age: " + age + "\n")
    #         break
    #     except:
    #         print("Invalid Age: ")

    # file_handle.write("Adress: " + input("Enter Address: \n") + "\n")
    # file_handle.write("Birthday: " + input("Enter Birthday: \n") + "\n")
    # file_handle.write("School: " + input("Enter School: \n") + "\n")
    # file_handle.write("Course: " + input("Enter Course: \n") + "\n")
    # file_handle.write("Year: " + str(int(input("Enter Year: \n"))) + "\n")
    # file_handle.write("Section: " + str(int(input("Enter Section: \n"))) + "\n")