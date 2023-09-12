"""
 Filename: AidansPrebuiltEmporium_V3.py
 Author: Aidan Newberry
 Created: 8/29/2023
 Version: 3
 Purpose: demonstrate fluid development
"""

import AidansPrebuilts_class as aidan

def Get_input():
        #TODO: Get int input from user, how many prebuilts needed
        computers = int(input("Enter number of computers: "))
        return computers


def output():
    #TODO: Display transaction for customer
    number_of_computers = Prebuilt_Emporium.number_of_computers
    total_receipt = Prebuilt_Emporium.total_receipt
    
    print(f"Cost of {number_of_computers:,.2f} Computers ='s ${total_receipt:,.2f}")


number_of_computers = Get_input()

Prebuilt_Emporium = aidan.PrebuiltEmporium()

Prebuilt_Emporium.calculate(number_of_computers)

output()
