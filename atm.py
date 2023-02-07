class ATM:
    def __init__(self, user_name):
        self.password = 3333
        self.user_name = user_name
        self.balance = 10000
        self.choice = 0

    def check_balance(self):
        print("Hello ", self.user_name,", your balance = R", self.balance)

    def deposit(self):
        dep = int(input("Enter your deposit: R"))
        self.balance += dep
        print("\n deposit amount: R", dep)
        print("Hello ", self.user_name,", your balance = R", self.balance)

    def withdraw(self):
        wit = int(input("Enter the amount to withdraw: R"))
        if wit > self.balance:
            print("Hello ", self.user_name,", Insufficient balance")
        else:
            self.balance -= wit
            print("\n Hello ", self.user_name,", withdrawn amount: R", wit)
            print("Hello ", self.user_name,", your balance = R", self.balance)

    def menu(self):
        pin = int(input("Enter your Four digit pin\n"))
        if pin == self.password:
            while self.choice != 5:
                print("**** Menu ****")
                print("1 == balance")
                print("2 == deposit")
                print("3 == withdraw")
                print("4 == cancel")
                print("5 == logout\n")

                self.choice = int(input("\nEnter your option:\n"))

                if self.choice == 1:
                    self.check_balance()
                elif self.choice == 2:
                    self.deposit()
                elif self.choice == 3:
                    self.withdraw()
                elif self.choice == 4:
                    print("\n session Ended!! Goodbye")
                elif self.choice == 5:
                    print("\n Logging out! Goodbye ")
                    break
                else:
                    print("\nInvalid Entry!!")
       

if __name__ == "__main__":
    user_name = input("Enter your name:")
    print("Welcome to AMR Bank\n\nInsert your card")
    atm = ATM(user_name)
    atm.menu()
