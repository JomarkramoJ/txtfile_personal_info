with open("./information_list.py", "a") as file_handle:
    file_handle.write("Name: " + input("Enter Name: \n") + "\n")
    while True:
        try:
            age = str(int(input("Enter Age: ")))
            file_handle.write("Age: " + age + "\n")
            break
        except:
            print("Invalid Age: ")

    file_handle.write("Adress: " + input("Enter Address: \n") + "\n")
    file_handle.write("Birthday: " + input("Enter Birthday: \n") + "\n")
    file_handle.write("School: " + input("Enter School: \n") + "\n")
    file_handle.write("Course: " + input("Enter Course: \n") + "\n")
    file_handle.write("Year: " + str(int(input("Enter Year: \n"))) + "\n")
    file_handle.write("Section: " + str(int(input("Enter Section: \n"))) + "\n")