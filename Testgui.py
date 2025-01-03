from tkinter import *
from tkinter import ttk
import os
import sys

def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Windurr:

	def __init__(self, master):

		master.title("My Application!")
		#master.size('640', '480')
		master.resizable(False, False)
		master.configure(background = '#FFFFFF')
		self.style = ttk.Style()
		self.style.configure('TFrame', background = '#FFFFFF')
		self.style.configure('TLabel', background = '#FFFFFF', font = ('Courier', 11))
		self.style.configure('Header.TLabel', font = ('Courier', 18, 'bold'), justify = 'center')

		self.frame_header = ttk.Frame(master)
		self.frame_header.pack()
		self.logo_small = PhotoImage(file=resource_path('pythonlogo.gif')).subsample(15,15)
		self.header_text = "If you are reading this, then something worked."
		label1 = ttk.Label(self.frame_header, style = 'Header.TLabel', text = self.header_text, image = self.logo_small, compound = 'left')
		button1 = ttk.Button(self.frame_header, text='Quit Me!', command = self.buhbye)

		label1.grid(row=0, column=0, padx = 10, pady = 10, ipady = 10, ipadx = 10)
		button1.grid(row=1, column=0, padx = 10, pady = 10, ipady = 10, ipadx = 10)

	def buhbye(self):
		exit()

def main():

	root = Tk()
	windurr = Windurr(root)
	root.mainloop()
	
if __name__ == "__main__":

	main()

