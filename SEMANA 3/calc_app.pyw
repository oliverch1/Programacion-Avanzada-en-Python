# -*- coding: utf-8 -*-
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(0, 0)
        self.config(bg='black')
        
        self.var_num = tk.StringVar(value='0')
        self.first_num = 0
        self.var_op = None
        self.solved = False
        
        CFG_DISPLAY_ARIAL = {'font': ('Arial', 16, 'bold'),
                       'textvariable': self.var_num, 
                       'justify': 'right', 
                       'state': 'readonly', 
                       'readonlybackground': '#A0E0A0', 
                       'width': 19}
        
        CFG_DISPLAY_LCD = {'font': ('Digital-7 Mono', 22, 'bold'),
                       'textvariable': self.var_num, 
                       'justify': 'right', 
                       'state': 'readonly', 
                       'readonlybackground': '#A0E0A0', 
                       'width': 16}
        
        CFG_BUTTON_GRAY = {'font': ('Arial', 12, 'bold'), 
                           'width': 4, 'bg': 'gray'}
        CFG_BUTTON_RED = {'font': ('Arial', 12, 'bold'), 
                          'width': 4, 'bg': 'red'}
        CFG_BUTTON_ORANGE = {'font': ('Arial', 12, 'bold'), 
                             'width': 4, 'bg': 'orange'}
        
        # Frame
        frm = tk.Frame(self, bg='black')
        frm.pack(padx=1, pady=10)
        
        try:
            tk.Entry(frm, CFG_DISPLAY_LCD).grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        except:
            tk.Entry(frm, CFG_DISPLAY_ARIAL).grid(row=0, column=0, columnspan=4, padx=5, pady=5)
                
        tk.Button(frm, CFG_BUTTON_GRAY, text="0", command=lambda: self.update_display('0')).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='we')
        tk.Button(frm, CFG_BUTTON_GRAY, text="1", command=lambda: self.update_display('1')).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text="2", command=lambda: self.update_display('2')).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text="3", command=lambda: self.update_display('3')).grid(row=4, column=2, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text="4", command=lambda: self.update_display('4')).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text="5", command=lambda: self.update_display('5')).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text="6", command=lambda: self.update_display('6')).grid(row=3, column=2, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text="7", command=lambda: self.update_display('7')).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text="8", command=lambda: self.update_display('8')).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text="9", command=lambda: self.update_display('9')).grid(row=2, column=2, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_GRAY, text=".", command=lambda: self.update_display('.')).grid(row=5, column=2, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_ORANGE, text="=", command=self.solve).grid(row=4, column=3, rowspan=2, padx=5, pady=5, sticky='ns')
        tk.Button(frm, CFG_BUTTON_ORANGE, text="+", command=lambda: self.set_operation('+')).grid(row=2, column=3, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_ORANGE, text="-", command=lambda: self.set_operation('-')).grid(row=3, column=3, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_ORANGE, text="÷", command=lambda: self.set_operation('/')).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_ORANGE, text="x", command=lambda: self.set_operation('*')).grid(row=1, column=3, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_RED, text="C", command=self.clear).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frm, CFG_BUTTON_RED, text="AC", command=self.clear_display).grid(row=1, column=1, padx=5, pady=5)
        
        self.bind_all('<Key>', self.set_key)
        
        
    def set_key(self, e):
        if e.char in '0123456789.':
            self.update_display(e.char)
            
        elif e.char in '+-*/':
            self.set_operation(e.char)
            
        elif e.keysym == 'Return':
            self.solve()
            
        elif e.keysym == 'Escape':
            self.clear()
        
            
    def update_display(self, char: str) -> None:
        if self.solved:
            self.clear()
            
        if self.var_num.get() == '0' or self.var_num.get() == 'E':
            self.var_num.set('')
            
        if char == '.' and self.var_num.get() == '':
            self.var_num.set('0.')
            
        if len(self.var_num.get()) < 12:
            if char == '.' and self.var_num.get().count('.') > 0:
                return None
            
            self.var_num.set(self.var_num.get() + char)
            
            
    def set_operation(self, op: str) -> None:
        self.var_op = op
        self.first_num = float(self.var_num.get())
        self.clear_display()
                    
        
        
    def solve(self):
        if self.var_op == '+':
            result = self.first_num + float(self.var_num.get())
        elif self.var_op == '-':
            result = self.first_num - float(self.var_num.get())
        elif self.var_op == '*':
            result = self.first_num * float(self.var_num.get())
        elif self.var_op == '/':
            try:
                result = self.first_num / float(self.var_num.get())
            except ZeroDivisionError:
                result = 'E'
        
        result = str(result)[:12]
        if result.endswith('.0'):
            result = result[:-2]
        
        self.var_op = None
        self.var_num.set(result)
                
        self.solved = True
            
        
            
    def clear(self) -> None:
        self.solved = False
        self.var_op = None
        self.first_num = 0
        self.clear_display()
                
        
    def clear_display(self) -> None:
        self.var_num.set('0')

        
if __name__ == "__main__":
    Calculator().mainloop()  
