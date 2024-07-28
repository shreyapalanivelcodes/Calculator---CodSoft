import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("300x200")
        
        self.create_widgets()

    def create_widgets(self):
        self.num1_label = tk.Label(self.master, text="Enter first number:")
        self.num1_label.pack(pady=5)
        
        self.num1_entry = tk.Entry(self.master, width=20)
        self.num1_entry.pack(pady=5)
        
        self.num2_label = tk.Label(self.master, text="Enter second number:")
        self.num2_label.pack(pady=5)
        
        self.num2_entry = tk.Entry(self.master, width=20)
        self.num2_entry.pack(pady=5)
        
        self.operation_label = tk.Label(self.master, text="Select operation:")
        self.operation_label.pack(pady=5)
        
        self.operation_var = tk.StringVar(value="add")
        self.add_radio = tk.Radiobutton(self.master, text="Add", variable=self.operation_var, value="add")
        self.add_radio.pack(pady=2)
        
        self.subtract_radio = tk.Radiobutton(self.master, text="Subtract", variable=self.operation_var, value="subtract")
        self.subtract_radio.pack(pady=2)
        
        self.multiply_radio = tk.Radiobutton(self.master, text="Multiply", variable=self.operation_var, value="multiply")
        self.multiply_radio.pack(pady=2)
        
        self.divide_radio = tk.Radiobutton(self.master, text="Divide", variable=self.operation_var, value="divide")
        self.divide_radio.pack(pady=2)
        
        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=10)
        
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=5)
        
    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = num1 / num2
            else:
                raise ValueError("Invalid operation selected.")
                
            self.result_label.config(text=f"Result: {result}")
        
        except ValueError as e:
            messagebox.showerror("Input Error", f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
