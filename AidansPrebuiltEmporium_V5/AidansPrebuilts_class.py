"""
 Filename: AidansPrebuiltEmporium_V5.py
 Author: Aidan Newberry
 Created: 8/29/2023
 Version: 5
 Purpose: demonstrate fluid development
"""

COMPUTER_COST = 999.0

class PrebuiltEmporium():
    def __init__(self) -> None:
        pass

    def get_number_of_computers(self):
        # validation
        if self.number_of_computers > 0:
            return self.number_of_computers
        else:
            
            return "You must order at least 1 computer"

    def get_total_sale(self):
        return self.total_receipt

    def calculate(self, number_of_computers):
        #TODO: Calculate cost of computers purchased
        self.number_of_computers = number_of_computers
        self.total_receipt = number_of_computers * COMPUTER_COST