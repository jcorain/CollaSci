'''module to create the main interface of the gui'''

import tkinter as tk
from tkinter import ttk 

# create the root application 

root = tk.Tk()
root.title("CollaSci")

# create the tabControl

tabControl = ttk.Notebook(root)

# create the tabs 


tab_user = ttk.Frame(tabControl)
tabControl.add(tab_user, text = 'User')

tab_experiment = ttk.Frame(tabControl)
tabControl.add(tab_experiment, text = 'Experiment')

tab_material = ttk.Frame(tabControl)
tabControl.add(tab_material, text = 'Material')

tab_project = ttk.Frame(tabControl)
tabControl.add(tab_project, text = 'Project')

tab_data = ttk.Frame(tabControl)
tabControl.add(tab_data, text = 'Data')

tabControl.pack(expand = 1, fill = 'both')

root.mainloop()