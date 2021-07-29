from tkinter import *
from tkinter import ttk
def function(r):
    frame= Frame(r, bg= '#fed8b1')
    frame.place(relwidth= 1, relheight= 1)
    def back_button_function(*args):
        frame.destroy()
    title= Label(frame, text= 'Fill in the blank', font= ('tkfixedfont 15', 20, 'bold'), bg= '#fed8b1')
    title.place(relx= 0.3, rely= 0.1)
    question_label= Label(frame, text= 'Question', font= ('tkfixedfont 15', 12, 'italic'), bg= '#fed8b1')
    question_label.place(relx= 0.45, rely= 0.2)
    made_by= Label(frame, text= 'Made by Mikiyas kibrom', bg= '#fed8b1', fg= '#0000ff')
    made_by.place(relx= 0.7, rely= 0.05)
    options_list= [
        '10',
        '20',
        '30',
        '40',
        '50',
        '60'
    ]
    options= ttk.Combobox(frame, value= options_list)
    options.current(1)
    options.place(relx= 0.4, rely= 0.3)
    back_button= ttk.Button(frame, text= 'Back', command= back_button_function)
    back_button.place(relx= 0.001, rely= 0.94)