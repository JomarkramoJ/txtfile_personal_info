def find_user(file_path, search_name):
    try:
        with open(file_path, "r") as file:
            for line in file:
                user_info = eval(line.strip())
                if user_info.get("Name").lower() == search_name.lower():
                    return user_info
        return None
    except FileNotFoundError:
        print("The file does not exist.")
        return None

file_path = "./information_list.py"
search_name = input("Enter the full name to search: ").strip()

result = find_user(file_path, search_name)