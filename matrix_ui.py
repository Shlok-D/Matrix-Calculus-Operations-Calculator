from sympy import *
import tkinter as tk
from tkinter import *
import matrix_classes as m
import sympy as sp
#import sys
#import os


class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows
        self.columns = columns

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")

        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                if self._entry[index].get() == '':
                    current_row.append(0)
                else:
                    current_row.append(int(self._entry[index].get()))
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True

    def clear_frame(self):
        for widgets in tk.Frame.winfo_children(self):
            widgets.destroy()


class PolynomialInput(tk.Frame):
    def __init__(self, parent, rows):
        tk.Frame.__init__(self, parent)

        self._entry = {}
        self.rows = rows

        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")
        s = "abcdefghijklmnopqrstuvwxyz"
        # create the table of widgets
        for row in range(self.rows):
            txt = s[row] + " ="
            l = tk.Label(self, text=txt, bg='#89CFF0')
            l.grid(row=row, column=1, stick="nsew")
            index = row
            e = tk.Entry(self, validate="key", validatecommand=vcmd)
            e.grid(row=row, column=2, stick="nsew")
            self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(1):
            self.grid_columnconfigure(2, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        current_row = []
        for row in range(self.rows):
            index = row
            if self._entry[index].get() == '':
                current_row.append(0)
            else:
                current_row.append(int(self._entry[index].get()))

        return current_row

    def _validate(self, P):
        '''Perform input validation. 

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True


class Example1(tk.Frame):
    l = []

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='#89CFF0')
        self.table = SimpleTableInput(self, testRows.get(), testCols.get())
        self.parent = parent
        self.submit = tk.Label(self, text="Matrix 1 Input", bg='#89CFF0')
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="top")
        self.table1 = SimpleTableInput(self, testRows1.get(), testCols1.get())
        self.submit1 = tk.Label(self, text="Matrix 2 Input", bg='#89CFF0')
        self.table1.pack(side="top", fill="both", expand=True)
        self.submit1.pack(side="top")
        self.cal = tk.Button(self, text="Calculate",
                             command=self.calculate, bg='#b0e0e6')
        self.cal.pack(side="top", pady=10)

    def on_submit(self):
        print(self.table.get())

    def calculate(self):
        if(selection.get() == "Matrix Addition"):
            a = m.Matrix()
            c = a.addition(self.table.get(), self.table1.get())
            self.print_matrices(c, "Addition: ")
        if(selection.get() == "Matrix Subtraction"):
            a = m.Matrix()
            c = a.subtraction(self.table.get(), self.table1.get())
            self.print_matrices(c, "Subtraction: ")
        if(selection.get() == "Matrix Multiplication"):
            a = m.Matrix()
            c = a.multiplication(self.table.get(), self.table1.get())
            self.print_matrices(c, "Multiplication: ")
        if(selection.get() == "Determinant"):
            a = m.Matrix()
            c = a.determinant(self.table.get())
            self.print_matrices(c, "Determinant: ")
        if(selection.get() == "Inverse"):
            a = m.Matrix()
            c = a.inverse(self.table.get())
            self.print_matrices(c, "Inverse: ")
        if(selection.get() == "Transpose"):
            a = m.Matrix()
            c = a.transpose(self.table.get())
            self.print_matrices(c, "Transpose: ")
        if(selection.get() == "Power of"):
            a = m.Matrix()
            c = a.power_off(self.table.get(), testRows1.get())
            self.print_matrices(c, "Power of {}: ".format(testRows1.get()))

    def print_matrices(self, matrix, s):
        txt = str(matrix)
        txt = s+txt
        self.answer = tk.Label(self, text=txt, width=1000,
                               bg='#89CFF0', font=("", 10))
        self.answer.pack()


class Example2(tk.Frame):
    l = []

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='#89CFF0')
        self.table = SimpleTableInput(self, testRows.get(), testCols.get())
        self.parent = parent
        self.submit = tk.Label(self, text="Matrix Input", bg='#89CFF0')
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="top")
        self.cal = tk.Button(self, text="Calculate",
                             command=self.calculate, bg='#b0e0e6')
        self.cal.pack(side="top", pady=10)

    def calculate(self):
        if(selection.get() == "Determinant"):
            a = m.Matrix()
            c = a.determinant(self.table.get())
            self.print_matrices(c, "Determinant: ")
        if(selection.get() == "Inverse"):
            a = m.Matrix()
            c = a.inverse(self.table.get())
            self.print_matrices(c, "Inverse: ")
        if(selection.get() == "Transpose"):
            a = m.Matrix()
            c = a.transpose(self.table.get())
            self.print_matrices(c, "Transpose: ")
        if(selection.get() == "Power of"):
            a = m.Matrix()
            c = a.power_off(self.table.get(), testRows1.get())
            self.print_matrices(c, "Power of {}: ".format(testRows1.get()))

    def print_matrices(self, matrix, s):
        txt = str(matrix)
        txt = s + txt
        self.answer = tk.Label(self, text=txt, width=1000,
                               bg='#89CFF0', font=("", 10))
        self.answer.pack()


class Example3(tk.Frame):
    l = []

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='#89CFF0')
        self.table = PolynomialInput(self, testRows1.get()+1)
        self.parent = parent
        self.submit = tk.Label(
            self, text="Enter Coefficients of Polynomial", bg='#89CFF0')
        self.table.pack(side="top", fill="both", expand=True)
        self.submit.pack(side="top")
        self.cal = tk.Button(self, text="Calculate",
                             command=self.calculate, bg='#b0e0e6')
        self.cal.pack(side="top", pady=10)

    def calculate(self):
        a = m.Polynomial()
        b = a.calculate(self.table.get())
        self.print_matrices(b, "x = ")

    def print_matrices(self, matrix, s):
        txt = str(matrix)
        txt = s + txt
        self.answer = tk.Label(self, text=txt, width=1000,
                               bg='#89CFF0', font=("", 10))
        self.answer.pack()


def other():
    def integrate():
        x = sp.Symbol('x')
        if(eq2.get() == 0 and eq1.get() == 0):
            integral = sp.integrate(eq.get(), (x))
        else:
            integral = sp.integrate(eq.get(), (x, eq1.get(), eq2.get()))
        txt = "Integration Result : " + str(integral)
        i = Label(root, text=txt, bg='#89CFF0', font=("", 10))
        i.pack()
        # print(integral)

     # defines window

    # Creates a static txt label
    eq_static = Label(root, text='Write the equation f(x) :',
                      font=("Times New Roman", 8), bg='#89CFF0')
    eq_static.pack(padx=10)

    eq = tk.StringVar(value='4*x')
    eq_Entered = Entry(root, width=40, textvariable=eq)
    eq_Entered.pack(padx=10)
    # Calculate button

    eq_static = Label(root, text='Limits:\n(Keep 0 for Indefinite Integral)', font=(
        "Times New Roman", 8), bg='#89CFF0')
    eq_static.pack(padx=10)

    eq1 = tk.IntVar(value=0)
    eq1_Entered = Entry(root, width=15, textvariable=eq1)
    eq1_Entered.pack()
    eq2 = tk.IntVar(value=0)
    eq2_Entered = Entry(root, width=15, textvariable=eq2)
    eq2_Entered.pack()

    action = Button(root, text='Integrate', command=integrate, bg='#b0e0e6')
    action.pack(pady=10)


def other1():
    def differentiate():
        x = sp.Symbol('x')
        derivative = sp.diff(eq.get(), x)
        txt = "Differentiation Result : " + str(derivative)
        i = Label(root, text=txt, bg='#89CFF0', font=("", 10))
        i.pack()
        # print(derivative)
     # defines window
    # Creates a static txt label
    eq_static = Label(root, text='Write the equation f(x) : ',
                      font=("Times New Roman", 8), bg='#89CFF0')
    eq_static.pack(padx=10)

    eq = tk.StringVar(value='4*x')
    eq_Entered = Entry(root, width=40, textvariable=eq)
    eq_Entered.pack(padx=10)

    action1 = Button(root, text='Differentiate',
                     command=differentiate, bg='#b0e0e6')
    action1.pack(pady=10)


def other4():
    def differentiate_1():
        x = sp.Symbol('x')
        derivative = sp.diff(eq.get(), x)
        for i in range(eq1.get()-1):
            derivative = sp.diff(derivative, x)
        txt = "Multiple Differentiation Result : " + str(derivative)
        i = Label(root, text=txt, bg='#89CFF0', font=("", 10))
        i.pack()
        # print(derivative)
     # defines window
    # Creates a static txt label
    eq_static = Label(root, text='Write the equation f(x) : ',
                      font=("Times New Roman", 8), bg='#89CFF0')
    eq_static.pack(padx=10)

    eq = tk.StringVar(value='4*x**5')
    eq_Entered = Entry(root, width=40, textvariable=eq)
    eq_Entered.pack(padx=10)

    eq2_static = Label(root, text='Enter n (Number of times to Differentiate): ', font=(
        "Times New Roman", 8), bg='#89CFF0')
    eq2_static.pack(padx=10)
    eq1 = tk.IntVar(value=1)
    eq1_Entered = Entry(root, width=40, textvariable=eq1)
    eq1_Entered.pack(padx=10)

    action1 = Button(root, text='Differentiate',
                     command=differentiate_1, bg='#b0e0e6')
    action1.pack(pady=10)


def other3():
    def double_integrate():
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        if(eq2.get() == 0 and eq1.get() == 0 and eq3.get() == '0' and eq4.get() == '0'):
            integral = sp.integrate(eq.get(), (y), x)
        else:
            integral = sp.integrate(
                eq.get(), (y, eq3.get(), eq4.get()), (x, eq1.get(), eq2.get()))
        txt = "Double Integration Result : " + str(integral)
        i = Label(root, text=txt, bg='#89CFF0', font=("", 10))
        i.pack()
        # print(integral)

     # defines window

    # Creates a static txt label
    eq_static = Label(root, text='Write the equation f(x,y) :',
                      font=("Times New Roman", 8), bg='#89CFF0')
    eq_static.pack(padx=10)

    eq = tk.StringVar(value='4*x*y')
    eq_Entered = Entry(root, width=40, textvariable=eq)
    eq_Entered.pack(padx=10)
    # Calculate button

    eq_static = Label(root, text='Limits:\n(Keep 0 for Indefinite Integral) \n(Input limits of x & then y)', font=(
        "Times New Roman", 8), bg='#89CFF0')
    eq_static.pack(padx=10)

    eq1 = tk.IntVar(value=0)
    eq1_Entered = Entry(root, width=15, textvariable=eq1)
    eq1_Entered.pack()
    eq2 = tk.IntVar(value=0)
    eq2_Entered = Entry(root, width=15, textvariable=eq2)
    eq2_Entered.pack()
    eq3 = tk.StringVar(value=0)
    eq3_Entered = Entry(root, width=15, textvariable=eq3)
    eq3_Entered.pack()
    eq4 = tk.StringVar(value=0)
    eq4_Entered = Entry(root, width=15, textvariable=eq4)
    eq4_Entered.pack()

    action = Button(root, text='Integrate',
                    command=double_integrate, bg='#b0e0e6')
    action.pack(pady=10)


def display():
    a = Example1(root)
    b = Example2(root)
    if(selection.get() == "Matrix Addition" or selection.get() == "Matrix Subtraction" or selection.get() == "Matrix Multiplication"):
        a.pack(side="top", fill="both", expand=True)
    elif(selection.get() == "Determinant" or selection.get() == "Inverse" or selection.get() == "Transpose" or selection.get() == "Power of"):
        b.pack(side="top", fill="both", expand=True)
    elif(selection.get() == "Differentiation"):
        other1()
    elif(selection.get() == "Integration"):
        other()
    elif(selection.get() == "Double Integration"):
        other3()
    elif(selection.get() == "Roots of Polynomial"):
        c = Example3(root)
        c.pack(side="top", fill="both", expand=True)
    else:
        other4()


# def clear_text():
   #text.delete(0, END)


root = tk.Tk()
root.title('Matrix & Calculus Operations Calculator')
# root.geometry("1080x720")
root.configure(bg='#89CFF0')
Options_List = ["Matrix Multiplication", "Matrix Addition", "Determinant", "Inverse",
                "Transpose", "Power of", "Matrix Subtraction", "Differentiation",
                "Integration", "Double Integration", "Multiple Differentiation", "Roots of Polynomial"]
selection = StringVar(root)
selection.set(Options_List[2])

Instructions = Label(
    root, text="Welcome to the Matrix & Calculus Operations Calculator. Enter your Rows then Columns.", bg='#89CFF0')
Instructions.pack()

x = Label(root, text="Rows", width=5, bg='#89CFF0')
x.pack(side="left")
testRows = IntVar(root)
sizeRows = Entry(root, width=15, textvariable=testRows)
sizeRows.pack(side="left")

testCols = IntVar(root)
sizeRows = Entry(root, width=15, textvariable=testCols)
sizeRows.pack(side="left")

y = Label(root, text="Columns", width=7, bg='#89CFF0')
y.pack(side="left")

y1 = Label(root, text="Columns", width=7, bg='#89CFF0')
y1.pack(side="right")
testCols1 = IntVar(root)
sizeRows = Entry(root, width=15, textvariable=testCols1)
sizeRows.pack(side="right")

testRows1 = IntVar(root)
sizeRows = Entry(root, width=15, textvariable=testRows1)
sizeRows.pack(side="right")
x1 = Label(root, text="Rows", width=7, bg='#89CFF0')
x1.pack(side="right")
submit1 = tk.Label(
    root, text="Ignore for Determinant,\nInverse & Transpose. \n(Power of - Enter n in Row Box) \n Enter Order of Polynomial (R of P)", bg='#89CFF0')
submit1.pack(side="right")


updatE = Button(root, text="Submit", command=display, bg='#b0e0e6')
updatE.pack()

#Button(root,text="Clear", command=clear_text, font=('Helvetica bold',10)).pack(pady=5)


drop_down = OptionMenu(root, selection, *Options_List)
drop_down.pack(pady=5)

'''
def _on_mousewheel(event):
    root.canvas.yview_scroll(-1*(event.delta/120), "units")

root.canvas = Canvas(root)
root.canvas.bind_all("<MouseWheel>", _on_mousewheel(root.canvas))
...
'''


#frame = Frame(root)
#frame.pack(side="top", expand=True, fill="both")
# def clear_frame():
# for widgets in frame.winfo_children():
# widgets.destroy()
# this will clear frame and frame will be empty
# if you want to hide the empty panel then
# frame.pack_forget()


# Create a button to close the window
# Button(frame, text="Clear", font=('Helvetica bold', 10), command=
# clear_frame).pack(pady=20)
root.mainloop()
