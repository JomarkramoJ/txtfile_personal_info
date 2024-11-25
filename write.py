informations = []

def is_valid_name(input_string):
    if any(char.isdigit() for char in input_string):
        return False
    return True

while True:
    user_info = {}
    while True:    
        name = input("Please enter your full name: ")
        if is_valid_name(name):
            user_info["Name"] = name
            break
        else:
            print("Name cannot contain numbers. ")
    while True:
        try:
            age = int(input("Enter age: "))
            if age >= 123 and age <= 130:
                print("You now have the world record of being the oldest ever to live according to google")
                user_info["Age"] = age
                break
            elif age >= 0 and age <= 130:
                user_info["Age"] = age
                break
            else:
                print("invalid age")
        except:
            print("Enter a valid age ")
    while True:
        address = input("Enter your address: ")
        user_info["Address"] = address
        break
    for i in range(6):
        birthday = input("Enter your birthday (MMDDYYYY): ")
        if len(birthday) == 8 and birthday.isdigit():
            formatted_birthday = f"{birthday[:2]},{birthday[2:4]},{birthday[4:]}"
            print(f"Formatted birthday: {formatted_birthday}")
            user_info["Birthday"] = formatted_birthday
            break
        else:
            print("Please follow this format MMDDYYYY:")
    while True:
        school = input("Enter your school: ")
        user_info["School"] = school
        break
    while True:
        course = input("Enter your course: ")
        user_info["Course"] = course
        break
    for i in range(2):
        year_section = input("Enter your year and section: ")
        if len(year_section) == 2 and year_section.isdigit():
            fixed_year_section = f"{year_section[0]}-{year_section[1]}"
            print(f"Year and section: {fixed_year_section}")
            user_info["Year and Section"] = fixed_year_section
            break
        else:
            print("Please enter only 2 numbers, one for your current year and the other for your section: 17")
    
    informations.append(user_info)

    print(informations)

    # with open("./information_list.py", "a") as file_handle:
        

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