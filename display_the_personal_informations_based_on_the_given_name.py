with open("C:\\Users\\Alexander\\OneDrive\\Desktop\\one_or_more_entries_for_personal_informations_with_integration_of_text_file\\user(s)_informations.txt", "r") as database_2:
    lines = database_2.readlines()
    for line in lines:
        print(line.strip())