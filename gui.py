import tkinter as tk
import tkinter.messagebox as msgbox


def button_func():
    msgbox.showinfo("test click",
                    "passed")  # first parameter is the title, and the second one is the content of the info box


win = tk.Tk(screenName='Test', baseName=None, className='Machine Learning Tool',
            useTk=1)  # creating the main window and storing the window object in 'win'
win.geometry('500x200')
# create the widgets here
canvas = tk.Canvas(win, width=500, height=200)  # create canvas
txt = canvas.create_text(250, 10, text="This tool helps you create a machine learning model with gui")
choose_framework_txt = canvas.create_text(250, 40, text="Please choose a framework you would like to work with")
canvas.pack()
button = tk.Button(win, text="test click", width=10, height=5, command=button_func)
button.place(x=200, y=50)
win.mainloop()  # running the loop that works as a trigger
