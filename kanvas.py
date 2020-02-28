# Third-library import
from tkinter import *
from tkinter import messagebox

# Set up window
root = Tk()
root.geometry("509x750")
root.title("Kanvas, a shape drawing GUI")
last_shape = None

# Set up canvas
canvas = Canvas(root, width=501, height=401, borderwidth=0, highlightthickness=0)

# Four frames
frame_1 = Frame(root)
frame_2 = Frame(root)
frame_3 = Frame(root)
frame_4 = Frame(root)
frame_5 = Frame(root)

def draw():
	global last_shape

	conditions_met = True

	# Check if all the parameters are valid
	param_list = [param_entry_1.get(), param_entry_2.get(), param_entry_3.get(), param_entry_4.get()]
	for param in param_list:
		if not param.isdigit():
			if re.search('[a-zA-Z]', param):
				messagebox.showwarning("Warning", "Non-integer Values")
				conditions_met = False
			else:
				if int(param) < 0:
					messagebox.showwarning("Warning", "Negative Values")
					conditions_met = False
			break
	
	if conditions_met:
		width = canvas.winfo_width()-1
		height = canvas.winfo_height()-1

		# Check if any of the parameter dimensions are invalid
		if ((int(param_entry1.get()) > width) or (int(param_entry3.get()) > width) or (int(param_entry2.get()) > height) or (int(param_entry4.get()) > height)):
			message = "Invalid Size: Canvas width and height are " + str(width) + " and " + str(height) + " respectively!"
			messagebox.showwarning("Warning", message)
			conditions_met = False

	if conditions_met:
		shape = shape_option.get() # FIX THIS cmd VAR NAME, better variable name
		if color_option.get() == 1:
			color = "red"
		elif color_option.get() == 2:
			color == "green"
		elif color_option.get() == 3:
			color == "blue"
		else:
			color = "black"


		if shape == 1:
			# Draw rectangle
			if len(width_entry.get())<1:
				last_shape = canvas.create_rectangle(int(param_entry_1.get()), int(param_entry_2.get()), int(param_entry_3.get()), int(param_entry_4.get()), fill=color)
			else:
				last_shape = canvas.create_rectangle(int(param_entry_1.get()), int(param_entry_2.get()), int(param_entry_3.get()), int(param_entry_4.get()), fill=color, width=int(width_entry.get()))

		elif shape == 2:
			# Draw line
			if len(width_entry.get())<1:
				last_shape = canvas.create_line(int(param_entry_1.get()), int(param_entry_2.get()), int(param_entry_3.get()), int(param_entry_4.get()), fill=color)
			else:
				last_shape = canvas.create_line(int(param_entry_1.get()), int(param_entry_2.get()), int(param_entry_3.get()), int(param_entry_4.get()), fill=color, width=int(width_entry.get()))

		else:
			# Draw oval
			if len(width_entry.get())<1:
				last_shape = canvas.create_oval(int(param_entry_1.get()), int(param_entry_2.get()), int(param_entry_3.get()), int(param_entry_4.get()), fill=color)
			else:
				last_shape = canvas.create_oval(int(param_entry_1.get()), int(param_entry_2.get()), int(param_entry_3.get()), int(param_entry_4.get()), fill=color, width=int(width_entry.get()))

def delete_recent():
	"""Delete the most recent function."""
	global last_shape
	canvas.delete(last_shape)


# Create widgets
param_label_1 = Label(frame_1, text="Param 1").grid(row=0, column=0)
param_entry_1 = Entry(frame_1, width=25)
param_entry_1.grid(row=0, column=1, sticky=W) # split into two lines to successfully return the entry value, else receive none
param_label_2 = Label(frame_1, text="Param 2").grid(row=1, column=0)
param_entry_2 = Entry(frame_1, width=25)
param_entry_2.grid(row=1, column=1, sticky=W)
param_label_3 = Label(frame_1, text="Param 3").grid(row=2, column=0)
param_entry_3 = Entry(frame_1, width=25)
param_entry_3.grid(row=2, column=1, sticky=W)
param_label_4 = Label(frame_1, text="Param 4").grid(row=3, column=0)
param_entry_4 = Entry(frame_1, width=25)
param_entry_4.grid(row=3, column=1, sticky=W)

# Set up color and shape options
shape_option = IntVar()
rectangle_button = Radiobutton(frame_2, text="Rectangle", variable=shape_option, value=1, command=draw).grid(row=0)
line_button = Radiobutton(frame_2, text="Line", variable=shape_option, value=2, command=draw).grid(row=1)
oval_button = Radiobutton(frame_2, text="Oval", variable=shape_option, value=3, command=draw).grid(row=2)

width_label = Label(frame_3, text="Width").grid(row=0, column=0)
width_entry = Entry(frame_3, width=25)
width_entry.grid(row=0, column=1)

color_option = IntVar()
red_button = Radiobutton(frame_4, text="Red", variable=color_option, value=1, command=draw).grid(row=0)
green_button = Radiobutton(frame_4, text="Green", variable=color_option, value=2, comman=draw).grid(row=1)
blue_button = Radiobutton(frame_4, text="Blue", variable=color_option, value=3, command=draw).grid(row=2)

# Set up delete button
delete_button = Button(frame_5, text="Delete the most recent shape", command=delete_recent).grid(row=0)

# Put it all together
canvas.pack(padx=2, pady=2)
frame_1.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()

# Run the program
root.mainloop()