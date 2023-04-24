import tkinter as tk
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
from faker import Faker
from home import FileSelectPage,generator , demo
# Create the main window
root = tk.Tk()
root.title("Infographix")

# Create a label for the title
title_label = tk.Label(root, text="Welcome to Infographix!", font=("Helvetica", 20))
title_label.pack()

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create buttons to navigate to other pages

# button_generate = tk.Button(root, text="generate file ", command=generator, bg='green')
# button_generate.pack()

button1_generate = tk.Button(root, text="Demo", command=demo)
# button1_generate = tk.Button(root, text="Search for student", command=lambda: (generator(), demo()), bg='#C0C0C0')
button1_generate.pack()

file_select_page = FileSelectPage(root)
file_select_page.pack()


# Create a label for the footer
#footer_label = tk.Label(root, text="Copyright © 2023 My Company")
#footer_label.pack(side=tk.BOTTOM, padx=10, pady=10)

# Run the main loop
root.mainloop()
