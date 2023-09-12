"""
 Filename: AidansPrebuiltEmporium_V3.py
 Author: Aidan Newberry
 Created: 8/29/2023
 Version: 3
 Purpose: demonstrate fluid development
"""

COMPUTER_COST = 999.0

class PrebuiltEmporium():
    def __init__(self) -> None:
        pass

    def calculate(self, number_of_computers):
        #TODO: Calculate cost of computers purchased
        self.number_of_computers = number_of_computers
        self.total_receipt = number_of_computers * COMPUTER_COST