import tkinter as tk

#Create the main application window(root)
root = tk.Tk()
root.title('Benevolent God - Grading Assistant')
root.geometry('600x150')

#global variable for keeping track of which scale to use for the calculation
level_var = 'lower'


def errormsg(msg):
    popup = tk.Tk()
    popup.wm_title("Error!")
    pop_label = tk.Label(popup, text = msg)
    pop_label.pack(side = "top", fill = "x", pady = 10)
    B1 = tk.Button(popup, text="Ok", command = popup.destroy)
    B1.pack()
    popup.mainloop()

#popup msg function, sample taken from pythonprogramming.net
def popupmsg(msg):
    popup = tk.Tk()
    popup.geometry('150x150')
    popup.wm_title("Results")
    pop_label = tk.Label(popup, text = msg)
    pop_label.pack(side = "top", fill = "x", pady = 10)
    B1 = tk.Button(popup, text="Okay", command = lambda: [popup.destroy(), label.config(text = 'Fill in the maximum amount of points achievable in the test, then click the calculate button.')])
    B1.pack()
    popup.mainloop()

# Create a function to handle button click event
def button_calculate():
    points_var = float(0)
    if points_entry.get() != '':
        if str(points_entry.get()).isnumeric():
            points_var = float(points_entry.get())
        else:
            errormsg('Wrong format! Input the maximum amount of points as a NUMBER')
    else:
        errormsg('You must fill in the maximum amount of points first!')
    label.config(text = 'Your results are shown in the popup window.')

    level_handle = level_var
    print(level_var)
    print(level_handle)
    match level_handle:
        case 'lower':
            scale = [10.0, 25.0, 35.0, 20.0, 10.0]
            result = [points_var / 100 * val  for val in scale]

        case 'upper':
            scale = [10.0, 17.0, 17.0, 28.0, 28.0]
            result = [points_var / 100 * val  for val in scale]

        case _:
            errormsg('Missing scale!')
    #console debug print to check the results against the set scale
    #print('Point distribution:')
    #print(result)
    grades = []
    for i in range(1, len(result)):
        grades.append(str(round(points_var - sum(result[0:i]) - 1)) + ' - ' + str(round(points_var - sum(result[0:(i+1)]), ndigits = 2)) + ': ' + str(i+1))
    popupmsg('Grade ranges:' '\n' + str(round(points_var)) + ' - ' + str(round(points_var - result[0])) + ': 1' + '\n' + str(grades[0])+ '\n' + str(grades[1]) + '\n' + str(grades[2]) + '\n' + str(grades[3]))

#set functions for the global variable level_var, used in the buttons to switch between the two, will most likely be replaced by lambda fns
def setLevel(val):
    global level_var
    level_var = val

ll_button = tk.Button(master = root, text = 'Lower level', command = lambda: setLevel('lower'))
ul_button = tk.Button(master = root, text = 'Upper lever', command = lambda: setLevel('upper'))
ll_button.pack(side = 'top')    
ul_button.pack(side = 'top')

headlabel = tk.Label(master = root, text = 'Max. Points', justify = 'center')
headlabel.pack()
# Entry for maximum points
points_entry = tk.Entry(master = root, width = 5, borderwidth = 3, justify = 'center') 
points_entry.pack()

#Adding 'Widgets' to the main window(root) - text label, calculate button
label = tk.Label(master = root, text = 'Fill in the maximum amount of points achievable in the test, then click the calculate button.')
label.pack()

button = tk.Button(master = root, text = 'Calculate', command = button_calculate)
button.pack(side = 'bottom')

#Mainloop to run the application keep the root window open till closed 
#(either manually, like in this case, or by fn() like in the case of the results popup window)
root.mainloop()
