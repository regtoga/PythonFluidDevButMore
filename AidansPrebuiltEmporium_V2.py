"""
 Filename: AidansPrebuiltEmporium_V2.py
 Author: Aidan Newberry
 Created: 8/29/2023
 Version: 2
 Purpose: demonstrate fluid development
"""

COMPUTER_COST = 999.0

def main():

    computers = get_input()
    total_receipt = calculate(computers)
    output(computers, total_receipt)

def get_input():
    #TODO: Get int input from user, how many prebuilts needed
    computers = int(input("Enter number of computers: "))
    return computers

def calculate(computers):
    #TODO: Calculate cost of computers purchased
    total_receipt = computers * COMPUTER_COST
    return total_receipt

def output(computers, total_receipt):
    #TODO: Display transaction for customer
    print(f"Cost of {computers:,.2f} Computers ='s ${total_receipt:,.2f}")

if __name__ == '__main__':
    main()