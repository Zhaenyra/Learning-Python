#Python and TKinter Message Box
#Most Important Lines to Remember
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.withdraw()   # hides the blank window
name = input("What is your name? ")
totalprice=int(input("Enter total price: "))
if totalprice>= 50000:
    discount= 0.2*totalprice
elif totalprice>= 30000:
    discount= 0.1*totalprice
elif totalprice>= 10000:
    discount= 0.05*totalprice
else:
    discount = 0
if discount == 0:
    messagebox.showwarning("No Discount", f"Hello {name}!\nYou get no discount today!")
else:
    messagebox.showinfo("Shopping Discount", f"Hello {name}!\nOriginal price: ₦{totalprice}\nDiscount:       ₦{round(discount,2)}\nFinal price:    ₦{totalprice - discount}")