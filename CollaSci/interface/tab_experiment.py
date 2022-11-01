'''
module to develop the experiment tab of the GUI
'''
import tkinter as tk
from tkinter import ttk

import CollaSci.db_function.database_utils as database_utils
import CollaSci.db_function.tables_update as table_update

import CollaSci.interface.GUI_utils as GUI_utils

class ExperimentWidget(tk.Frame):
    def __init__(self, parent, connection):
        
        # define the frame for the user tab
        tk.Frame.__init__(self, parent)
        create_experiment_tabs(self, connection)

class ExperimentTypeTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        
       #  define the first label holding the already defined users 
        self.label_experiment_type = tk.Label(self, text = 'Registered experiment types', relief = 'ridge')
        self.label_experiment_type.pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_type')
            if res is not None:
                # define columns 
            
                col = ('id','name')    
                
                # initiate treeview
                
                self.experiment_type_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
                # define headings
                
                self.experiment_type_tree.heading('id', text = 'id')
                self.experiment_type_tree.heading('name', text = 'Name')
            
                # get the values related to the experiment type table
                
                val = None
                for experiment_type in res:
                    val = (experiment_type[0],
                           experiment_type[1])
                    self.experiment_type_tree.insert('',tk.END, values = val)

                self.experiment_type_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(self, connection, 'experiment_type', parent)
                GUI_utils.AddButton(self, connection, 'experiment_type', parent)

                
            else:
                self.label_no_experiment_type = tk.Label(self, text = 'There is no data in the experiment_type table')
                self.label_no_experiment_type.pack()    

                
        else:
            self.label_no_experiment_type = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_experiment_type.pack()    

class ExperimentTypeAdd():
    def __init__(self, popup, connection, grandparent):
        # add the first name values 
        self.name_lab = tk.Label(popup, text = 'Name')
        self.name_lab.pack()
        
        # define the firstname string value 
        
        name = tk.StringVar(popup)
        
        # get the entry for firstname 
       
        self.name_entry = tk.Entry(popup, textvariable = name)
        self.name_entry.pack()
                
        # add the add button 
        
        self.add_user_button = tk.Button(popup, text = 'Add user column', command = lambda : add_experiment_type_col(popup, name, connection, grandparent))
        self.add_user_button.pack()


def add_experiment_type_col(popup, name, connection, grandparent):
    
    table_update.add_row_experiment_type_table(name.get(), connection)
    
    # update the user table 
    popup.destroy()

    GUI_utils.update_table('user', connection, grandparent)


def create_experiment_tabs(widget, connection):     
    # define the new tabs with user, status, laboratory and university 
    widget.tabcontrol_experiment = ttk.Notebook(widget)
    
    widget.tab_experiment_type = ExperimentTypeTree(widget.tabcontrol_experiment, connection)
    widget.tabcontrol_experiment.add(widget.tab_experiment_type, text = 'Experiment Type')
    
    # widget.tab_experiment_setup = StatusTree(widget.tabcontrol_experiment, connection)
    # widget.tabcontrol_experiment.add(widget.tab_experiment_setup, text = 'Experiment Setup')
        
    widget.tabcontrol_experiment.pack(expand = 1, fill = 'both')