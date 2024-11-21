call_name = input("Enter the name: ") 
final_call_name = "Name: " + call_name

with open("C:\\Users\\Alexander\\OneDrive\\Desktop\\one_or_more_entries_for_personal_informations_with_integration_of_text_file\\user(s)_informations.txt", "r") as database_2:
    lines = database_2.readlines()
    for line in range(len(lines)):
        if lines[line].strip() == final_call_name:
            print(lines[line].strip())
            print(lines[line + 1].strip())
            print(lines[line + 2].strip())
            print(lines[line + 3].strip())
            print(lines[line + 4].strip())
            print(lines[line + 5].strip())
            break
    else:
        print(f"'{call_name}' was not found in the file.")