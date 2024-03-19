import tkinter as tk

class Calculator:
    def __init__(self, a):
        self.a = a
        a.title("Calculator")

        # Entry widget to display input and output
        self.display = tk.Entry(a, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button labels
        buttons = [
            ('7',1,0),('8',1,1),('9',1,2),('+',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('-',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('*',3,3),
            ('0',4,0),('%',4,1),('.',4,2),('/',4,3),
            ('=',5,1),('C',5,2)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(a, text=text, padx=20, pady=20,
                               command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def calculate_percentage(self):
        try:
            result = eval(self.display.get()) / 100
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def button_click(self, value):
        current = self.display.get()
        if value == '=':
            try:
                result = eval(current)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == 'C':
            self.display.delete(0, tk.END)
        elif value == 'C':
            self.display("")
        elif value == '%':
            self.calculate_percentage()
        else:
            self.display.insert(tk.END, value)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
