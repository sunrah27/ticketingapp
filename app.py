class Ticket:
    def __init__(self, adultPrice=20, childPrice=12, seniorPrice=11):
        self.adultPrice = adultPrice
        self.childPrice = childPrice
        self.seniorPrice = seniorPrice
        self.adultQty = 0
        self.childQty = 0
        self.seniorQty = 0
        self.has_parking = False

    def inputTicketQuantity(self):
        while True:
            try:
                self.adultQty = int(input("Enter the number of adult tickets: "))
                break
            except ValueError:
                print("Please enter a valid number for adult tickets.")

        while True:
            try:
                self.childQty = int(input("Enter the number of child tickets: "))
                break
            except ValueError:
                print("Please enter a valid number for child tickets.")

        while True:
            try:
                self.seniorQty = int(input("Enter the number of senior tickets: "))
                break
            except ValueError:
                print("Please enter a valid number for senior tickets.")

    def requireParking(self):
        while True:
            response = input("Do you require parking? (yes/no): ").lower()
            if response in ["yes", "y"]:
                self.hasParking = True
                break
            elif response in ["no", "n"]:
                self.hasParking = False
                break
            else:
                print("Please enter 'yes' or 'no'.")

    @property
    def totalChild(self):
        return self.childQty * self.childPrice

    @property
    def totalAdult(self):
        return self.adultQty * self.adultPrice

    @property
    def totalSenior(self):
        return self.seniorQty * self.seniorPrice

    @property
    def grandTotal(self):
        return self.totalChild + self.totalAdult + self.totalSenior

def receipt(ticketManager):
    print(" -------------------------------------------")
    print("| Ticket type | Price (£) | Qty | Total(£)  |")
    print(" -------------------------------------------")
    print(f"| Adult       |       £{ticketManager.adultPrice} |   {ticketManager.adultQty} |       £{ticketManager.totalAdult} |")
    print(" -------------------------------------------")
    print(f"| Child       |       £{ticketManager.childPrice} |   {ticketManager.adultQty} |       £{ticketManager.totalChild} |")
    print(" -------------------------------------------")
    print(f"| Senior      |       £{ticketManager.seniorPrice} |   {ticketManager.adultQty} |       £{ticketManager.totalSenior} |")
    print(" -------------------------------------------")
    print(f"| Grant dotal                   |       £{ticketManager.grandTotal}|")
    print(" -------------------------------------------")

def ticketBookingProcess():
    ticketManager = Ticket()
    print("Welcome to Adventures Inc Theme Park\nWe have a wide variety of attractions for all ages\nPlease let me know what I can help you with?\nFor example: type 'ticket prices' to see ticket prices or 'book tickets' to book tickets.")
    
    while True:
        option = input("How can I be of service>? ").lower()
        
        if option == 'ticket prices':
            print("Ticket prices:")
            print(f"Adult: £{ticketManager.adultPrice}")
            print(f"Child: £{ticketManager.childPrice}")
            print(f"Senior: £{ticketManager.seniorPrice}")
        elif option == 'book tickets':

            ticketManager.inputTicketQuantity()
            ticketManager.requireParking()

            print(f"Total cost of adult tickets: £{ticketManager.totalAdult}")
            print(f"Total cost of child tickets: £{ticketManager.totalChild}")
            print(f"Total cost of senior tickets: £{ticketManager.totalSenior}")
            print(f"Grand total: £{ticketManager.grandTotal}")
            print("Thank you for chosing Adventures Inc Theme Park. We wish you a wonderful time.")
            receipt(ticketManager)
            break
        else:
            print("Please type 'ticket prices' to see ticket prices or 'book tickets' to book tickets.")

if __name__ == "__main__":
    ticketBookingProcess()