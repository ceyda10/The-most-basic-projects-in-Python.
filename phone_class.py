import os
class PhoneBook :
    def __init__(self):
        self.file_name = "Files/phonebook.txt"
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w", encoding="utf-8") as f:
                pass
    def add_contact(self, first_name, last_name, phone):
        with open(self.file_name, "a", encoding="utf-8") as f:
            f.write(f"{first_name},{last_name},{phone}\n")
            print(f"{first_name} {last_name} added to phonebook.")
    def list_contact(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("Phonebook is empty.")
            else:
                for line in lines:
                    first_name, last_name, phone = line.strip().split(",")
                    print(f"{first_name} {last_name} -{phone}")
    def delete_contact(self, name):
        found = False
        with open(self.file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(self.file_name, "w", encoding="utf-8") as f:
            for line in lines:
                first_name, last_name, phone = line.strip().split(",")
                if first_name != name:
                    f.write(line)
                else:
                    found = True
        if found:
            print(f"{name} deleted from phonebook.")
        else: 
            print(f"{name} not found in phonebook.")
                
                
                    
            
