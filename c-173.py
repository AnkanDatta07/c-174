# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:27:46 2023

@author: Ankan Datta
"""
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root =Tk()
root.geometry("900x500")



class parent():
    def __init__(self):
        print("This is parent class.")
        
    def menu(dish):
        if dish == "Burger":
            print("You can add following toppins - ")
            print("More cheese|jelapeno")
            
        elif dish == "Iced Americano":
            print("You can add following toppins - ")
            print("Add Chocolate Flavour|Add Caramel Flavour")
            
        else:
            print("please enter valid dish.")
            
    def final_amount(dish, add_ons):
        if dish == "Burger" and add_ons == "More Cheese":
            print("You need to pay 250 USD")
        if dish == "Burger" and add_ons == "Jelapeno":
            print("You need to pay 350 USD")
        if dish == "Iced Americano" and add_ons == "Add Chocolate Flavour":
            print("You need to pay 250 USD")
        if dish == "Iced Americano" and add_ons == "Add Caramel Flavour":
            print("You have to pay 450 USD")
            
class child1(parent):
    def __init__(self, dish):
        self.new_dish = dish
        
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    def __init__(self, dish, addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish, self.addons)
        
child1_object = child1("Burger")
child1_object.get_menu()

child2_object = child2("Burger", "Jelapeno")
child2_object.get_final_amount()

child1_object = child1("Iced Americano")
child1_object.get_menu()

child2_object = child2("Iced Americano", "Add Caramel Flavour")
child2_object.get_final_amount()

child1_object = child1("Pizza")
child1_object.get_menu()

child2_object = child2("Pizza", "More Cheese")
child2_object.get_final_amount()















