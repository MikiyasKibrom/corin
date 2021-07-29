from tkinter import *
from tkinter import ttk
import false_10question
import false_20questions
import false_30question
def function(r):
	frame= Frame(r, bg= '#fed8b1')
	frame.place(relwidth= 1, relheight= 1)
	def back_button_function(*args):
		frame.destroy()
	def Combobox_function(*args):
		if options.get() == options_list[0]:
			false_10question.function(r)
		if options.get() == options_list[1]:
			false_20questions.function(r)
		if options.get() == options_list[2]:
			false_30question.function(r)
	title= Label(frame, text= 'True/False', bg= '#fed8b1', font= ('tkfixedfont 15', 20, 'bold'))
	title.place(relx= 0.4, rely= 0.1)
	questions_label= Label(frame, text= 'Question', font= ('tkfixedfont 15', 12, 'italic'), bg= '#fed8b1')
	questions_label.place(relx= 0.45, rely= 0.2)
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
	options_stringvar= StringVar(frame)
	options_stringvar.set(options_list[1])
	options= ttk.Combobox(frame, value= options_list)
	options.current(0)
	options.bind('<<ComboboxSelected>>', Combobox_function)
	options.place(relx= 0.45, rely= 0.3)
	back_button= ttk.Button(frame, text= 'Back', command= back_button_function)
	back_button.place(relx= 0.001, rely= 0.94)