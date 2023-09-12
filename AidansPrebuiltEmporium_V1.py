"""
 Filename: AidansPrebuiltEmporium_V1.py
 Author: Aidan Newberry
 Created: 8/29/2023
 Version: 1
 Purpose: demonstrate fluid development
"""

COMPUTER_COST = 999.0

#TODO: Get int input from user, how many prebuilts needed
computers = int(input("Enter number of computers: "))

#TODO: Calculate cost of computers purchased

total_receipt = computers * COMPUTER_COST

print(f"Cost of {computers:,.2f} Computers ='s ${total_receipt:,.2f}")