"""
 Filename: AidansPrebuiltEmporium_V5.py
 Author: Aidan Newberry
 Created: 8/29/2023
 Version: 6
 Purpose: demonstrate fluid development
"""

import AidansPrebuilts_class as aidan

def Get_Case():
        #TODO: Get int input from user hot many cases needed
        qty_Case = int(input("Enter number of Cases: "))
        return qty_Case

def Get_CPU():
        #TODO: Get int input from user hot many cases needed
        qty_CPU = int(input("Enter number of CPUS: "))
        return qty_CPU

def Get_Motherboard():
        #TODO: Get int input from user hot many cases needed
        qty_Mobo = int(input("Enter number of Motherboards: "))
        return qty_Mobo

def Get_GPU():
        #TODO: Get int input from user hot many cases needed
        qty_GPU = int(input("Enter number of GPUS: "))
        return qty_GPU

def Get_Storage():
        #TODO: Get int input from user hot many cases needed
        qty_Storage = int(input("Enter number of Storage devices: "))
        return qty_Storage

def Get_RAM():
        #TODO: Get int input from user hot many cases needed
        qty_RAM = int(input("Enter number of Ram Sticks: "))
        return qty_RAM

def Get_Power_Supply():
        #TODO: Get int input from user hot many cases needed
        qty_Power_Supply = int(input("Enter number of Power Supplies: "))
        return qty_Power_Supply

def Get_CPU_Cooler():
        #TODO: Get int input from user hot many cases needed
        qty_CPU_Cooler = int(input("Enter number of CPU coolers: "))
        return qty_CPU_Cooler

def Get_Fan():
        #TODO: Get int input from user hot many cases needed
        qty_Fan = int(input("Enter number of Fans: "))
        return qty_Fan


def display_order(qty_Case, qty_CPU, qty_Mobo, qty_GPU, qty_Storage, qty_RAM, qty_Power_Supply, qty_Fan) -> str:
    # TODO: Display transaction for customer
    """Display menu items2ws and prices"""
    # for n in range(3):
    #     print(f"{self.menu_items[n]} {self.menu_prices[n]}")
    Order_component_items = [qty_Case, qty_CPU, qty_Mobo, qty_GPU, qty_Storage, qty_RAM, qty_Power_Supply, qty_Fan]
    Order_component_prices = Prebuilt_Emporium.get_Component_prices()

    display = ""
    for n in range(len(Order_component_items)):
        i = n + 1
        display += f"({i}) {Order_component_items[n]} {Order_component_prices[n] * Order_component_items[n]:.2f}\n"
    return display


#Create PrebuiltEmpoium object
Prebuilt_Emporium = aidan.PrebuiltEmporium()

menu = Prebuilt_Emporium.display_catalouge()
print(menu)
#Get number of parts from users
qty_Case = Get_Case()
qty_CPU = Get_CPU()
qty_Mobo = Get_Motherboard()
qty_GPU = Get_GPU()
qty_Storage = Get_Storage()
qty_RAM = Get_RAM()
qty_Power_Supply = Get_Power_Supply()
qty_Fan = Get_Fan()

print(display_order(qty_Case, qty_CPU, qty_Mobo, qty_GPU, qty_Storage, qty_RAM, qty_Power_Supply, qty_Fan))
