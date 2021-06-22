import tkinter as tk
import math
window =tk.Tk()
window.title('Calculator')
window.geometry('500x630')
window.resizable(False, False)
window.configure(bg = 'black')
# Fun count
def calculate(operation):

    global formula

    if operation == 'C':
        formula = '0'
    elif operation == '<-':
        formula = formula[0:-1]
    elif operation == '=':
        formula = str(eval(formula))
    elif operation == 'sin':
        formula = str(math.sin(float(formula)))
    elif operation == 'cos':
        formula = str(math.cos(float(formula)))
    elif operation == 'tg':
        formula = str(math.tan(float(formula)))
    elif operation == 'ctg':
        formula = str(math.cos(float(formula))/math.sin(float(formula)))
    elif operation == 'log':
        formula = str(math.log10(float(formula)))
    elif operation == 'ln':
        formula = str(math.log(float(formula)))
    elif operation == 'Bin':
        formula = str(bin(int(formula)))
    else:
        if formula == '0':
            formula = ''
        formula += operation
    label_text.configure(text=formula)


# Result show
formula = '0'
label_text = tk.Label(text= formula, font = ('Roboto',30, 'bold'), bg = 'black',fg = 'white')
label_text.place(x = 11, y = 50)

# button
buttons = ['C','<-', '+', '=','1','2','3', '/','4','5','6','*','7','8','9','cos','0','sin','tan','ctg','Bin','log','ln','%']
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    tk.Button(text= button, bg = 'orange', font=('Roboto', 20), command = get_lbl).place(x =x , y=y, width = 115, height = 79)
    x += 117
    if x > 400:
        x = 18
        y += 81


window.mainloop

