"""
 Filename: AidansPrebuiltEmporium_V3.py
 Author: Aidan Newberry
 Created: 8/29/2023
 Version: 3
 Purpose: demonstrate fluid development
"""
#define constants
COMPUTER_COST = 999.0

class PrebuiltEmporium():
    #when we create class because of init object program auto runs
    def __init__(self) -> None:
        pass
        #run all the functions 
        
    def input(self):
        #TODO: Get int input from user, how many prebuilts needed
        self.computers = int(input("Enter number of computers: "))

    def calculate(self):
        #TODO: Calculate cost of computers purchased
        self.total_receipt = self.computers * COMPUTER_COST

    def output(self):
        #TODO: Display transaction for customer
        print(f"Cost of {self.computers:,.2f} Computers ='s ${self.total_receipt:,.2f}")

Prebuilt_Emporium = PrebuiltEmporium()
#while true run the program
while True:
    Prebuilt_Emporium.input(), Prebuilt_Emporium.calculate(), Prebuilt_Emporium.output()
    
    
