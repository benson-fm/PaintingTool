import tkinter as tk 
from tkinter import ttk

def drawing_func(event):
    x = event.x
    y = event.y
    if var.get() == 'A':
        # label_var.set('Pen Tool Selected')
        if color.get() == 'bla':
            canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2), fill = 'black', outline = 'black') 
        elif color.get() == 'r':
            canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2), fill = 'red', outline = 'red')
        elif color.get() == 'blu':
            canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2), fill = 'blue', outline = 'blue')   
    if var.get() == 'B':
        canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2), fill = 'white', outline = 'white')
        # label_var.set('Eraser Tool Selected')

def change_size(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4
    brush_size = max(0, min(brush_size, 50))

def update_color(new_color):
    color.set(new_color)
    if var.get() == 'A':
        if color.get() == 'bla':
            label_var.set('Black Color Selected')
        elif color.get() == 'blu':
            label_var.set('Blue Color Selected') 
        elif color.get() == 'r':
            label_var.set('Red Color Selected')
def update_label():    
    if var.get() == 'A':
        label_var.set('Pen Tool Selected')
    elif var.get() == 'B':
        label_var.set('Eraser Tool Selected')

# def combine_funcs(*funcs):
#     def combined_func(*args, **kwargs):
#         for f in funcs:
#             f(*args, **kwargs)
#     return combined_func

# window
window = tk.Tk()
window.geometry('600x400')
window.title("Painter Tool")

# styling
ttk.Style().theme_use('clam')
style = ttk.Style()

style.configure('Black.TButton', background = 'black', foreground = 'black')
style.configure('Red.TButton', background = 'red', foreground = 'red')
style.configure('Blue.TButton', background = 'blue', foreground = 'blue')

# Label
label = tk.Label(window, text = 'Painter Tool', font = ('Arial', 24))
label.pack()

label_var = tk.StringVar(value = 'Welcome to Painter Tool!')
live_label = tk.Label(window, text = 'label', textvariable = label_var)
live_label.pack()

# canvas
canvas = tk.Canvas(window, bg = "white", width = 400, height = 350 )
canvas.pack(padx = 25, pady = 35, side = tk.LEFT)

# Buttons (colors)
color = tk.StringVar(value = 'bla')
blackButton = ttk.Button(window, style = 'Black.TButton', command = lambda: update_color('bla')).place(x = 450, y = 100, width = 20, height = 20)
redButton = ttk.Button(window, style = 'Red.TButton', command = lambda: update_color('r')).place(x = 475, y = 100, width = 20, height = 20)
blueButton = ttk.Button(window,style = 'Blue.TButton', command = lambda: update_color('blu')).place(x = 500, y = 100, width = 20, height = 20)


# Radiobuttons
var = tk.StringVar(value = 'A')
penButton = tk.Radiobutton(window, text = 'Pen', variable = var, value = 'A', command = update_label).place(x = 450, y = 150)
eraseButton = tk.Radiobutton(window, text = 'Erase', variable = var, value = 'B', command = update_label).place(x = 525, y = 150)


# explore later
# fillButton = ttk.Button(window, text = 'Pen', variable = var, value = 'A', command = drawing_func)

# Drawing Mechanic
brush_size = 4
canvas.bind('<B1-Motion>', drawing_func)
canvas.bind('<MouseWheel>', change_size)

# run
window.mainloop()