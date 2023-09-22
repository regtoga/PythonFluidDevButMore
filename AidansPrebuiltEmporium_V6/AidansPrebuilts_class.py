"""
 Filename: AidansPrebuiltEmporium_V5.py
 Author: Aidan Newberry
 Created: 8/29/2023
 Version: 6
 Purpose: demonstrate fluid development
"""

COMPUTER_COST = 999.0

class PrebuiltEmporium():
    def __init__(self):
        self.Component_items = ["Case", "CPU", "Motherboard" , "GPU", "Storage", "RAM", "Power Supply", "CPU Cooler", "Fan"]
        self.Component_prices = [98.99, 250, 140, 500, 200, 175.85, 130, 45, 19.99  ]
        #Initialize an empty cart
        self.cart = []

    def get_Component_items(self) -> list:
        return self.Component_items
    
    def get_Component_prices(self) -> list:
        return self.Component_prices

#----------------------- DISPLAY MENU ---------------------------------

    def display_catalouge(self) -> str:
        """Display menu items and prices"""
        # iterates though the lists of catalouge items
        #  and appends them to the display variable
        display = ""
        for n in range(len(self.Component_items)):
            i = n + 1
            display += f"({i}) {self.Component_items[n]} {self.Component_prices[n]:.2f}\n"
        return display

#------------------------- DISPLAY ORDER ----------------------------

    def display_order(self) -> str:
        """Display order"""
        # This is currently placeholder code
        display = ""
        for n in range(len(self.Component_items)):
            i = n + 1
            display += f"({i}) {self.Component_items[n]} {self.Component_prices[n]:.2f}\n"
        return display


#------------------------ GET Component QUANTITY ---------------------

    def get_number_of_computers(self) -> int:
        """Input validation-the customer must order
        at least one component"""
        if self._number_of_computers > 0:
            return self._number_of_computers
        else:
            
            return "You must order at least 1 computer"

    def get_total_sale(self) -> float:
        """Return total sale from object
            Returns:
            _total_sale (float)
        """
        return self.total_receipt

    def calculate(self, number_of_computers: int = 1):
        """Calculate cost of the hotdogs purchased

            Parameters:
            number_of_hotdogs (int)
        """
        self._number_of_computers = number_of_computers
        self._total_receipt = self._number_of_computers * COMPUTER_COST