#tkinter is use to create appliction
import tkinter as tk
from tkinter import filedialog
#matplotlib use to create graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#plt is use to plot 
import matplotlib.pyplot as plt
#pandas is use to read .csv file
import pandas as pd
#numpy is use to solve math problems
import numpy as np
#faker is uce create fake data
from faker import Faker



def IT():
    root = tk.Tk()  
    root.title("IT")
    df = pd.read_csv("data.csv")

    label_stname = tk.Label(root, text="Student name:")
    label_stname.pack()

    entry_stname = tk.Entry(root)
    entry_stname.pack()

    label_stsid = tk.Label(root, text="Student ID:")
    label_stsid.pack()

    entry_stsid = tk.Entry(root)
    entry_stsid.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    def Student(stname):
        data_it = df[df['stream'] == 'IT']
        st_data = data_it[data_it['name'] == stname]

        ia_cols = ['ia_math', 'ia_phy', 'ia_chem', 'ia_bee', 'ia_mecha']
        ese_cols = ['math', 'phy', 'chem', 'bee', 'mecha']
        
        ia_marks = np.array(st_data[ia_cols])
        ia_perc = np.mean(ia_marks, axis=0)*100/20

        ese_marks = np.array(st_data[ese_cols])
        ese_perc = np.mean(ese_marks, axis=0)*100/80

        fig5, ax = plt.subplots()
        ax.bar(ia_cols, ia_perc, label='IA Marks Percentage')
        ax.bar(ese_cols, ese_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('IA vs ESE Marks Percentage')
        ax.legend()

        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        subjects = ['Math', 'Phy', 'Chem', 'Bee', 'Mecha']
        ia_total_marks = np.sum(ia_marks, axis=1)
        ia_total_perc = ia_total_marks/20*100

        ese_total_marks = np.sum(ese_marks, axis=1)
        ese_total_perc = ese_total_marks/80*100

        fig6, ax = plt.subplots()
        ax.plot(subjects, ia_total_perc, label='IA Marks Percentage')
        ax.plot(subjects, ese_total_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('Subjects vs Total IA and ESE Marks Percentage')
        ax.legend()

        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.draw()
        canvas6.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    

    def on_graph_button_click():
        stname = entry_stname.get()
        Student(stname)

    Graph_button = tk.Button(button_frame, text="Graph", command=on_graph_button_click)
    Graph_button.pack(padx=5)

    root.mainloop()


def COMPS():
    root = tk.Tk()
    root.title("COMPS")
    df = pd.read_csv("data.csv")

    label_stname = tk.Label(root, text="Student name:")
    label_stname.pack()

    entry_stname = tk.Entry(root)
    entry_stname.pack()

    label_stsid = tk.Label(root, text="Student ID:")
    label_stsid.pack()

    entry_stsid = tk.Entry(root)
    entry_stsid.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    def Student(stname):
        data_COMPS = df[df['stream'] == 'COMPS']
        st_data = data_COMPS[data_COMPS['name'] == stname]

        ia_cols = ['ia_math', 'ia_phy', 'ia_chem', 'ia_bee', 'ia_mecha']
        ese_cols = ['math', 'phy', 'chem', 'bee', 'mecha']
        
        ia_marks = np.array(st_data[ia_cols])
        ia_perc = np.mean(ia_marks, axis=0)*100/20

        ese_marks = np.array(st_data[ese_cols])
        ese_perc = np.mean(ese_marks, axis=0)*100/80

        fig5, ax = plt.subplots()
        ax.bar(ia_cols, ia_perc, label='IA Marks Percentage')
        ax.bar(ese_cols, ese_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('IA vs ESE Marks Percentage')
        ax.legend()

        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        subjects = ['Math', 'Phy', 'Chem', 'Bee', 'Mecha']
        ia_total_marks = np.sum(ia_marks, axis=1)
        ia_total_perc = ia_total_marks/20*100

        ese_total_marks = np.sum(ese_marks, axis=1)
        ese_total_perc = ese_total_marks/80*100

        fig6, ax = plt.subplots()
        ax.plot(subjects, ia_total_perc, label='IA Marks Percentage')
        ax.plot(subjects, ese_total_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('Subjects vs Total IA and ESE Marks Percentage')
        ax.legend()

        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.draw()
        canvas6.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    

    def on_graph_button_click():
        stname = entry_stname.get()
        Student(stname)

    Graph_button = tk.Button(button_frame, text="Graph", command=on_graph_button_click)
    Graph_button.pack(padx=5)

    root.mainloop()



def MECH():
    root = tk.Tk()
    root.title("MECH")
    df = pd.read_csv("data.csv")

    label_stname = tk.Label(root, text="Student name:")
    label_stname.pack()

    entry_stname = tk.Entry(root)
    entry_stname.pack()

    label_stsid = tk.Label(root, text="Student ID:")
    label_stsid.pack()

    entry_stsid = tk.Entry(root)
    entry_stsid.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    def Student(stname):
        data_MECH = df[df['stream'] == 'MECH']
        st_data = data_MECH[data_MECH['name'] == stname]

        ia_cols = ['ia_math', 'ia_phy', 'ia_chem', 'ia_bee', 'ia_mecha']
        ese_cols = ['math', 'phy', 'chem', 'bee', 'mecha']
        
        ia_marks = np.array(st_data[ia_cols])
        ia_perc = np.mean(ia_marks, axis=0)*100/20

        ese_marks = np.array(st_data[ese_cols])
        ese_perc = np.mean(ese_marks, axis=0)*100/80

        fig5, ax = plt.subplots()
        ax.bar(ia_cols, ia_perc, label='IA Marks Percentage')
        ax.bar(ese_cols, ese_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('IA vs ESE Marks Percentage')
        ax.legend()

        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        subjects = ['Math', 'Phy', 'Chem', 'Bee', 'Mecha']
        ia_total_marks = np.sum(ia_marks, axis=1)
        ia_total_perc = ia_total_marks/20*100

        ese_total_marks = np.sum(ese_marks, axis=1)
        ese_total_perc = ese_total_marks/80*100

        fig6, ax = plt.subplots()
        ax.plot(subjects, ia_total_perc, label='IA Marks Percentage')
        ax.plot(subjects, ese_total_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('Subjects vs Total IA and ESE Marks Percentage')
        ax.legend()

        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.draw()
        canvas6.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    

    def on_graph_button_click():
        stname = entry_stname.get()
        Student(stname)

    Graph_button = tk.Button(button_frame, text="Graph", command=on_graph_button_click)
    Graph_button.pack(padx=5)

    root.mainloop()


def EXTC():
    root = tk.Tk()
    root.title("EXTC")
    df = pd.read_csv("data.csv")

    label_stname = tk.Label(root, text="Student name:")
    label_stname.pack()

    entry_stname = tk.Entry(root)
    entry_stname.pack()

    label_stsid = tk.Label(root, text="Student ID:")
    label_stsid.pack()

    entry_stsid = tk.Entry(root)
    entry_stsid.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    def Student(stname):
        data_EXTC = df[df['stream'] == 'EXTC']
        st_data = data_EXTC[data_EXTC['name'] == stname]

        ia_cols = ['ia_math', 'ia_phy', 'ia_chem', 'ia_bee', 'ia_mecha']
        ese_cols = ['math', 'phy', 'chem', 'bee', 'mecha']
        
        ia_marks = np.array(st_data[ia_cols])
        ia_perc = np.mean(ia_marks, axis=0)*100/20

        ese_marks = np.array(st_data[ese_cols])
        ese_perc = np.mean(ese_marks, axis=0)*100/80

        fig5, ax = plt.subplots()
        ax.bar(ia_cols, ia_perc, label='IA Marks Percentage')
        ax.bar(ese_cols, ese_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('IA vs ESE Marks Percentage')
        ax.legend()

        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        subjects = ['Math', 'Phy', 'Chem', 'Bee', 'Mecha']
        ia_total_marks = np.sum(ia_marks, axis=1)
        ia_total_perc = ia_total_marks/20*100

        ese_total_marks = np.sum(ese_marks, axis=1)
        ese_total_perc = ese_total_marks/80*100

        fig6, ax = plt.subplots()
        ax.plot(subjects, ia_total_perc, label='IA Marks Percentage')
        ax.plot(subjects, ese_total_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('Subjects vs Total IA and ESE Marks Percentage')
        ax.legend()

        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.draw()
        canvas6.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    

    def on_graph_button_click():
        stname = entry_stname.get()
        Student(stname)

    Graph_button = tk.Button(button_frame, text="Graph", command=on_graph_button_click)
    Graph_button.pack(padx=5)

    root.mainloop()


def ITs(file_path):
    root = tk.Tk()
    root.title("IT")
    df = pd.read_csv(file_path)

    label_stname = tk.Label(root, text="Student name:")
    label_stname.pack()

    entry_stname = tk.Entry(root)
    entry_stname.pack()

    label_stsid = tk.Label(root, text="Student ID:")
    label_stsid.pack()

    entry_stsid = tk.Entry(root)
    entry_stsid.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    def Student(stname):
        data_IT = df[df['stream'] == 'IT']
        st_data = data_IT[data_IT['name'] == stname]

        ia_cols = ['ia_math', 'ia_phy', 'ia_chem', 'ia_bee', 'ia_mecha']
        ese_cols = ['math', 'phy', 'chem', 'bee', 'mecha']
        
        ia_marks = np.array(st_data[ia_cols])
        ia_perc = np.mean(ia_marks, axis=0)*100/20

        ese_marks = np.array(st_data[ese_cols])
        ese_perc = np.mean(ese_marks, axis=0)*100/80

        fig5, ax = plt.subplots()
        ax.bar(ia_cols, ia_perc, label='IA Marks Percentage')
        ax.bar(ese_cols, ese_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('IA vs ESE Marks Percentage')
        ax.legend()

        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        subjects = ['Math', 'Phy', 'Chem', 'Bee', 'Mecha']
        ia_total_marks = np.sum(ia_marks, axis=1)
        ia_total_perc = ia_total_marks/20*100

        ese_total_marks = np.sum(ese_marks, axis=1)
        ese_total_perc = ese_total_marks/80*100

        fig6, ax = plt.subplots()
        ax.plot(subjects, ia_total_perc, label='IA Marks Percentage')
        ax.plot(subjects, ese_total_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('Subjects vs Total IA and ESE Marks Percentage')
        ax.legend()

        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.draw()
        canvas6.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    

    def on_graph_button_click():
        stname = entry_stname.get()
        Student(stname)

    Graph_button = tk.Button(button_frame, text="Graph", command=on_graph_button_click)
    Graph_button.pack(padx=5)

    root.mainloop()


def COMPSs(file_path):
    root = tk.Tk()
    root.title("COMPS")
    df = pd.read_csv(file_path)

    label_stname = tk.Label(root, text="Student name:")
    label_stname.pack()

    entry_stname = tk.Entry(root)
    entry_stname.pack()

    label_stsid = tk.Label(root, text="Student ID:")
    label_stsid.pack()

    entry_stsid = tk.Entry(root)
    entry_stsid.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    def Student(stname):
        data_COMPS = df[df['stream'] == 'COMPS']
        st_data = data_COMPS[data_COMPS['name'] == stname]

        ia_cols = ['ia_math', 'ia_phy', 'ia_chem', 'ia_bee', 'ia_mecha']
        ese_cols = ['math', 'phy', 'chem', 'bee', 'mecha']
        
        ia_marks = np.array(st_data[ia_cols])
        ia_perc = np.mean(ia_marks, axis=0)*100/20

        ese_marks = np.array(st_data[ese_cols])
        ese_perc = np.mean(ese_marks, axis=0)*100/80

        fig5, ax = plt.subplots()
        ax.bar(ia_cols, ia_perc, label='IA Marks Percentage')
        ax.bar(ese_cols, ese_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('IA vs ESE Marks Percentage')
        ax.legend()

        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        subjects = ['Math', 'Phy', 'Chem', 'Bee', 'Mecha']
        ia_total_marks = np.sum(ia_marks, axis=1)
        ia_total_perc = ia_total_marks/20*100

        ese_total_marks = np.sum(ese_marks, axis=1)
        ese_total_perc = ese_total_marks/80*100

        fig6, ax = plt.subplots()
        ax.plot(subjects, ia_total_perc, label='IA Marks Percentage')
        ax.plot(subjects, ese_total_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('Subjects vs Total IA and ESE Marks Percentage')
        ax.legend()

        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.draw()
        canvas6.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    

    def on_graph_button_click():
        stname = entry_stname.get()
        Student(stname)

    Graph_button = tk.Button(button_frame, text="Graph", command=on_graph_button_click)
    Graph_button.pack(padx=5)

    root.mainloop()

def EXTCs(file_path):
    root = tk.Tk()
    root.title("EXTC")
    df = pd.read_csv(file_path)

    label_stname = tk.Label(root, text="Student name:")
    label_stname.pack()

    entry_stname = tk.Entry(root)
    entry_stname.pack()

    label_stsid = tk.Label(root, text="Student ID:")
    label_stsid.pack()

    entry_stsid = tk.Entry(root)
    entry_stsid.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    def Student(stname):
        data_EXTC = df[df['stream'] == 'EXTC']
        st_data = data_EXTC[data_EXTC['name'] == stname]

        ia_cols = ['ia_math', 'ia_phy', 'ia_chem', 'ia_bee', 'ia_mecha']
        ese_cols = ['math', 'phy', 'chem', 'bee', 'mecha']
        
        ia_marks = np.array(st_data[ia_cols])
        ia_perc = np.mean(ia_marks, axis=0)*100/20

        ese_marks = np.array(st_data[ese_cols])
        ese_perc = np.mean(ese_marks, axis=0)*100/80

        fig5, ax = plt.subplots()
        ax.bar(ia_cols, ia_perc, label='IA Marks Percentage')
        ax.bar(ese_cols, ese_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('IA vs ESE Marks Percentage')
        ax.legend()

        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        subjects = ['Math', 'Phy', 'Chem', 'Bee', 'Mecha']
        ia_total_marks = np.sum(ia_marks, axis=1)
        ia_total_perc = ia_total_marks/20*100

        ese_total_marks = np.sum(ese_marks, axis=1)
        ese_total_perc = ese_total_marks/80*100

        fig6, ax = plt.subplots()
        ax.plot(subjects, ia_total_perc, label='IA Marks Percentage')
        ax.plot(subjects, ese_total_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('Subjects vs Total IA and ESE Marks Percentage')
        ax.legend()

        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.draw()
        canvas6.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    

    def on_graph_button_click():
        stname = entry_stname.get()
        Student(stname)

    Graph_button = tk.Button(button_frame, text="Graph", command=on_graph_button_click)
    Graph_button.pack(padx=5)

    root.mainloop()


def MECHs(file_path):
    root = tk.Tk()
    root.title("MECH")
    df = pd.read_csv(file_path)

    label_stname = tk.Label(root, text="Student name:")
    label_stname.pack()

    entry_stname = tk.Entry(root)
    entry_stname.pack()

    label_stsid = tk.Label(root, text="Student ID:")
    label_stsid.pack()

    entry_stsid = tk.Entry(root)
    entry_stsid.pack()

    button_frame = tk.Frame(root)
    button_frame.pack()

    def Student(stname):
        data_MECH = df[df['stream'] == 'MECH']
        st_data = data_MECH[data_MECH['name'] == stname]

        ia_cols = ['ia_math', 'ia_phy', 'ia_chem', 'ia_bee', 'ia_mecha']
        ese_cols = ['math', 'phy', 'chem', 'bee', 'mecha']
        
        ia_marks = np.array(st_data[ia_cols])
        ia_perc = np.mean(ia_marks, axis=0)*100/20

        ese_marks = np.array(st_data[ese_cols])
        ese_perc = np.mean(ese_marks, axis=0)*100/80

        fig5, ax = plt.subplots()
        ax.bar(ia_cols, ia_perc, label='IA Marks Percentage')
        ax.bar(ese_cols, ese_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('IA vs ESE Marks Percentage')
        ax.legend()

        canvas5 = FigureCanvasTkAgg(fig5, master=root)
        canvas5.draw()
        canvas5.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        subjects = ['Math', 'Phy', 'Chem', 'Bee', 'Mecha']
        ia_total_marks = np.sum(ia_marks, axis=1)
        ia_total_perc = ia_total_marks/20*100

        ese_total_marks = np.sum(ese_marks, axis=1)
        ese_total_perc = ese_total_marks/80*100

        fig6, ax = plt.subplots()
        ax.plot(subjects, ia_total_perc, label='IA Marks Percentage')
        ax.plot(subjects, ese_total_perc, label='ESE Marks Percentage')
        ax.set_xlabel('Subjects')
        ax.set_ylabel('Percentage')
        ax.set_title('Subjects vs Total IA and ESE Marks Percentage')
        ax.legend()

        canvas6 = FigureCanvasTkAgg(fig6, master=root)
        canvas6.draw()
        canvas6.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

    

    def on_graph_button_click():
        stname = entry_stname.get()
        Student(stname)

    Graph_button = tk.Button(button_frame, text="Graph", command=on_graph_button_click)
    Graph_button.pack(padx=5)

    root.mainloop()