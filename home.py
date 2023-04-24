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
import os
from faker import Faker
from streams import IT,COMPS,EXTC,MECH,ITs,COMPSs,EXTCs,MECHs
import csv

def generator():
    root = tk.Tk()
    select_dept = tk.Label(root, text="Select Department", width=10)
    select_dept.grid(row=0,column=0)
    #it button
    IT_button = tk.Button(root, text="IT", command=IT, width=10)
    IT_button.grid(row=1, column=0, padx=5)
    #comps
    Comps_button = tk.Button(root, text="COMPS", command=COMPS , width=10)
    Comps_button.grid(row=1, column=1, padx=5)
    #
    MECH_button = tk.Button(root, text="MECH", command=MECH, width=10)
    MECH_button.grid(row=1, column=2, padx=5)
    #
    Extc_button = tk.Button(root, text="EXTC", command=EXTC, width=10)
    Extc_button.grid(row=1, column=3, pady=5)
    fake = Faker()
    sid = []
    name=[]
    stream=[]
    ia_math= []
    ia_phy=[]
    ia_chem=[]
    ia_bee=[]
    ia_mecha=[]
    math=[]
    phy=[]
    chem=[]
    bee=[]
    mecha=[]
    gender=[]
    orals=[]
    for _ in range(240) :
        gender.append(np.random.choice(('M','F','Rather not say'), p=(0.7,0.299,0.001)))
        ia_math.append(np.random.randint(0,20))
        ia_phy.append(np.random.randint(0,20))
        ia_chem.append(np.random.randint(0,20))
        ia_bee.append(np.random.randint(0,20))
        ia_mecha.append(np.random.randint(0,20))
        math.append(np.random.randint(10,80))
        phy.append(np.random.randint(10,60))
        chem.append(np.random.randint(10,60))
        bee.append(np.random.randint(10,80))
        mecha.append(np.random.randint(10,80))
        orals.append(np.random.randint(0,10))
                
    print(ia_math)
    print(ia_phy)
    print(ia_chem)
    print(ia_bee)
    print(ia_mecha)
    print(math)
    print(phy)
    print(chem)
    print(bee)
    print(mecha)
    print(gender)
    print(orals)
    #name generator
    for i in range(0, len(gender)):
         
        if gender[i]== 'M':
            name.append(fake.name_male())
        elif gender[i] == 'F' :
            name.append(fake.name_female())
        else : 
            name.append(fake.name_nonbinary())
          
    print(name)

    id_no=1
    for i in range(0, len(gender)):
        choice = stream.append(np.random.choice(('IT','COMPS','EXTC', 'MECH'), p=(0.25,0.25,0.25,0.25)))
        year = "2022"
        if choice == 'IT':
            rec = year + "1300"
        if choice == 'COMPS':
            rec = year + "1400"
        if choice == 'EXTC':
            rec = year + "1200"
        else :
            rec = year + "1100"
        if id_no < 10 :
            num = "00" + str(id_no)
        elif id_no < 100 :
            num = "0" + str(id_no)
        else :
            num = str(id_no)
        rec = rec + num
        id_no += 1
        sid.append(rec)
    print(stream)
    print(sid)
    academic_data = pd.DataFrame(zip(sid,stream,name,gender,ia_math,ia_phy,ia_chem,ia_bee,ia_mecha,math,phy,chem,bee,mecha,orals),columns=['sid','stream','name','gender','ia_math','ia_phy','ia_chem','ia_bee','ia_mecha','math','phy','chem','bee','mecha','orals'])
    dataset = academic_data.to_csv('data.csv', index = False)
    df = pd.read_csv('data.csv')
    grouped_data1 = df.groupby('stream')['ia_math','ia_phy','ia_chem','ia_bee','ia_mecha'].mean()
    grouped_data1.plot(kind='bar')
    plt.title('Stream vs IA')
    plt.xlabel('Stream')
    plt.ylabel('Avg. Marks')
    # plt.show()
    fig1 = plt.gcf()

    # Create a frame to hold the first graph
    frame1 = tk.Frame(root)
    frame1.pack(side=tk.LEFT, padx=10, pady=10)

    canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    grouped_data2 = df.groupby('stream')['math','phy','chem','bee','mecha'].mean()
    grouped_data2.plot(kind='bar')
    plt.title('Stream vs ESE Marks')
    plt.xlabel('Stream')
    plt.ylabel('Avg. Marks')
    # plt.show()
    fig2 = plt.gcf()
    # Create a frame to hold the second graph
    frame2 = tk.Frame(root)
    frame2.pack(side=tk.RIGHT, padx=10, pady=10)
    canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Start the tkinter event loop
    tk.mainloop()

    
    root.mainloop()

def demo():
    root = tk.Tk()
    #it button
    IT_button = tk.Button(root, text="IT", command=IT, width=10)
    IT_button.grid(row=0, column=0, padx=5, pady=5)
    #comps
    Comps_button = tk.Button(root, text="COMPS", command=COMPS , width=10)
    Comps_button.grid(row=0, column=1, padx=5, pady=5)
    #
    MECH_button = tk.Button(root, text="MECH", command=MECH, width=10)
    MECH_button.grid(row=0, column=2, padx=5, pady=5)
    #
    Extc_button = tk.Button(root, text="EXTC", command=EXTC, width=10)
    Extc_button.grid(row=0, column=3, pady=5, padx=5)
    




class FileSelectPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Create a button to open the file dialog box
        self.button = tk.Button(self, text="Select Files", command=self.open_file_dialog)
        self.button.pack(pady=10)

        # Create a label to display the selected file paths
        self.file_label = tk.Label(self, text="")
        self.file_label.pack()

        # Create a Next button (but don't show it yet)
        self.Next_button = tk.Button(self, text="Graph", command=lambda: self.Next_page(self.file_path), state=tk.DISABLED)
        self.Next_button.pack()

        # Placeholder for file path
        self.file_path = None

    def open_file_dialog(self):
        # Open the file dialog box and allow the user to select one or more files
        file_paths = filedialog.askopenfilenames()

        if len(file_paths) == 0:
            return

        # Extract the base name of each file path
        file_names = [os.path.basename(path) for path in file_paths]

        # Update the file label to display the selected file names
        self.file_label.config(text=", ".join(file_names))

        # Provide the full path to the file when reading it
        self.file_path = file_paths[0]
        self.Next_button.config(state=tk.NORMAL)

    def read_csv_file(self, file_paths):
        if not os.path.isfile(file_paths):
            print("Error: File not found. Please check the file path and try again.")
            return None
        try:
            df = pd.read_csv(file_paths)
            return df
        except FileNotFoundError:
            print("Error: File not found. Please check the file path and try again.")

    def Next_page(self, file_path):
        root = tk.Toplevel()
        
         #it button
        IT_button = tk.Button(root, text="IT", command=lambda: ITs(file_path), width=10)
        IT_button.grid(row=0, column=0, padx=5, pady=5)
       
        #comps
        Comps_button = tk.Button(root, text="COMPS", command=lambda: COMPSs(file_path), width=10)
        Comps_button.grid(row=0, column=1, padx=5, pady=5)
        #
        MECH_button = tk.Button(root, text="MECH", command=lambda: MECHs(file_path), width=10)
        MECH_button.grid(row=0, column=2, padx=5, pady=5)
        #
        Extc_button = tk.Button(root, text="EXTC", command=lambda: EXTCs(file_path), width=10)
        Extc_button.grid(row=0, column=3, padx=5, pady=5)

        # Pack the buttons into the root window

    


  

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Analysis")
    #create button 
    button_generate = tk.Button(root, text="generate file ", command=generator)
    button_generate.pack()

    file_select_page = FileSelectPage(root)
    file_select_page.pack()

    tk.mainloop()



