from tkinter import *
from tkinter import ttk
import false
import matching
import Choice
import ff
import fill
root= Tk()
root.geometry('750x500')
root.title('Corin')
root.resizable(False, False)
root.iconbitmap('tick.ico')
def options_command(*args):
	if options.get() == options_list[0]:
		false.function(root)
	if options.get() == options_list[1]:
		matching.function(root)
	if options.get() == options_list[2]:
		Choice.function(root)
	if options.get() == options_list[3]:
		ff.function(root)
	if options.get() == options_list[4]:
		fill.function(root)
frame= Frame(root, bg= '#fed8b1')
frame.place(relwidth= 1, relheight= 1)
def exit_button_function(*args):
	root.quit()
title= Label(frame, text= 'Corin', font= ('tkfixedfont 15', 30, 'bold'), bg= '#fed8b1')
title.place(relx= 0.4, rely= 0.1)
mode_label= Label(frame, text= 'Modes', font= ('tkfixedfot 15', 12, 'italic'), bg= '#fed8b1')
mode_label.place(relx= 0.48, rely= 0.3)
made_by= Label(frame, text= 'Made by Mikiyas kibrom', fg= 'blue', bg= '#fed8b1')
made_by.place(relx= 0.7, rely= 0.05)
options_list= [
	'True/False',
	'Matching',
	'Choice',
	'Answer the ff',
	'Fill in the blank',
	'All'
]
options_stringvar= StringVar(frame)
options_stringvar.set(options_list[0])
options= ttk.Combobox(frame, value= options_list)
options.current(0)
options.bind('<<ComboboxSelected>>', options_command)
options.place(relx= 0.4, rely= 0.4)
exit_button= ttk.Button(frame, text= 'Exit', command= exit_button_function)
exit_button.place(relx= 0.001, rely= 0.93)
root.mainloop()