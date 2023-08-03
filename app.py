import tkinter as tk 
from tkinter import ttk

def drawing_func(event):
    x = event.x
    y = event.y
    if var.get() == 'A':
        canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2), fill = 'black', outline = 'black')
    if var.get() == 'B':
        canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2), fill = 'white', outline = 'white')

def change_size(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4
    brush_size = max(0, min(brush_size, 50))

# window
window = tk.Tk()
window.geometry('600x400')
window.title("Painter Tool")

# canvas
canvas = tk.Canvas(window, bg = 'white', width = 400, height = 350 )
canvas.pack(padx = 25, pady = 25, side = tk.LEFT)

# Radiobuttons
var = tk.StringVar(value = 'A')
penButton = ttk.Radiobutton(window, text = 'Pen', variable = var, value = 'A', command = drawing_func).place(x = 500, y = 150)
eraseButton = ttk.Radiobutton(window, text = 'Erase', variable = var, value = 'B', command = drawing_func).place(x = 500, y = 200)


# explore later
# fillButton = ttk.Button(window, text = 'Pen', variable = var, value = 'A', command = drawing_func)

# Drawing Mechanic
brush_size = 4
canvas.bind('<B1-Motion>', drawing_func)
canvas.bind('<MouseWheel>', change_size)



# run
window.mainloop()