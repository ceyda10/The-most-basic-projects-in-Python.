import os
def prepare_system(dir_name="data", file_name="ledger.txt"):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Folder created: {dir_name}")
    else:
        print(f"Folder already exists: {dir_name}")
    file_path = os.path.join(dir_name, file_name)
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("[SYSTEM INITIALIZED]\n")
    return file_path
class SecureLedger:
    def __init__(self, dir_name="data", file_name="ledger.txt"):
        self.__file_path = prepare_system(dir_name, file_name)
    @property
    def file_path(self):
        return self.__file_path
    def get_file_size(self):
        return os.path.getsize(self.__file_path)
    def add_transaction(self, transaction_type, amount, description):
     entry = f"[{transaction_type}] {amount} TL - {description}\n"
     with open(self.__file_path, "a+", encoding="utf-8") as f:
         f.write(entry)
         f.flush()
         print(f"Transaction recorded: {entry.strip()}")
    def get_balance(self):
        total_balance = 0.0
        with open(self.__file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("[INCOME]"):
                    parts = line.split()
                    amount = float(parts[1])
                    total_balance += amount
                elif line.startswith("[EXPENSE]"):
                    parts = line.split()
                    amount = float(parts[1])
                    total_balance -= amount
        return total_balance
    def update_header(self):
        current_balance = self.get_balance()
        new_header =f"AUDIT SUMMARY | BALANCE: {current_balance} TL\n"
        with open(self.__file_path, "r+", encoding="utf-8") as f:
            lines = f.readlines()
            lines[0] = new_header
            f.seek(0)
            f.writelines(lines)
            f.truncate()
            f.flush()
    def dump_audit_log(self):
        with open(self.__file_path, "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())      
if __name__ == "__main__":
    vault = SecureLedger()
    print("File Path:", vault.file_path)
    print("File Size(bytes):", vault.get_file_size())
    try:
        vault.file_path = "hacker.txt"
    except AttributeError as e:
        print("Security Check Passed! Error:", e)
    vault.add_transaction("INCOME", 2500, "Scholorship deposited")
    vault.add_transaction("EXPENSE", 450, "Grocery  shopping")
    print("Post-Transaction File Size:", vault.get_file_size())
    print("Current Vault Balance:", vault.get_balance())
    vault.update_header()
    vault.dump_audit_log()
    
 
        


    
    
                
        

    
