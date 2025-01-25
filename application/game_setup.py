from tkinter import simpledialog, messagebox
from domain.character import Character  

def setup_game():
    Pet_name = simpledialog.askstring("Input", "Enter your Pet's name:")

    if Pet_name:
        pet = Character(Pet_name)
        messagebox.showinfo("Pet Created", f"Your pet, {pet.name}, has been created!")
    else:
        messagebox.showerror("Error", "You must enter a name for your pet!")
        return None

    return pet  
