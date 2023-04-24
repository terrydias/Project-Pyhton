import tkinter as tk
from tkinter import ttk
import plotly.graph_objs as go
import plotly.offline as pyo
from tkhtmlview import HTMLLabel
import pandas as pd

# Load the data
df = pd.read_csv('data.csv')

# Filter the data by stream = EXTC
data_extc = df[df['stream'] == 'EXTC']

# Calculate the mean of ESE marks by subject for the EXTC stream
grouped_data = data_extc.groupby('stream')['math', 'ia_math'].mean().reset_index()

# Create the bar plot
fig = go.Figure()
fig.add_trace(go.Bar(x=grouped_data['stream'], y=grouped_data['math'], name='ESE Marks'))
fig.add_trace(go.Bar(x=grouped_data['stream'], y=grouped_data['ia_math'], name='IA Marks'))
fig.update_layout(title='EXTC Stream: Average IA and ESE Marks by Subject',
                  xaxis_title='Subject',
                  yaxis_title='Marks',
                  barmode='group')

# Save the plot to a HTML file
pyo.plot(fig, filename='extc_marks.html', auto_open=False)

# Create the tkinter window
root = tk.Tk()

# Create a label to display the Plotly graph in HTML format
label = HTMLLabel(root, html='<iframe src="extc_marks.html" width="100%" height="100%" style="border:none;"></iframe>')
label.pack(fill="both", expand=True)

# Run the tkinter event loop
root.mainloop()
