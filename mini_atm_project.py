balance = 10000
while True:
  choice = input("Please select the action you wish to perform (1,2,3,4): ")
  if choice == "1":
      print(f"Your current balance is {balance}")
  elif choice == "2":
      amount =int(input("How much do you want to deposit?"))
      balance += int(amount)
      print(f"Deposit succesful. Your new balance is: {balance}")
  elif choice  == "3":
      amount = int(input("Please enter the amount you wish to withdraw:"))
      if amount <= balance:
          balance -= amount
          print(f"Wİthdrawal successful. YOur new balance is {balance}")
      else:
          print("Insufficient balance!")
  elif choice == "4":
      print("Thank you for using our bank. Logging out... Have a nice day!")
      break
  else:
      print("Invalid choice. Please try again.")
    
    
    