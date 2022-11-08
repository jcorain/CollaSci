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


class ExperimentSetupTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        
       #  define the first label holding the already defined users 
        self.label_experiment_setup = tk.Label(self, text = 'Registered experiment setups', relief = 'ridge')
        self.label_experiment_setup.pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_setup')
            if res is not None:
                # define columns 
            
                col = ('id','name','room_name','start_date','min_field','max_field',
                       'min_temp','max_temp','experiment_type','responsible_name')    
                
                # initiate treeview
                
                self.experiment_setup_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
                # define headings
                
                self.experiment_setup_tree.heading('id', text = 'id')
                self.experiment_setup_tree.heading('name', text = 'Name')
                self.experiment_setup_tree.heading('room_name', text = 'Room Name')
                self.experiment_setup_tree.heading('start_date', text = 'Start Date')
                self.experiment_setup_tree.heading('min_field', text = 'Minimum Field (T)')
                self.experiment_setup_tree.heading('max_field', text = 'Maximum Field (T)')
                self.experiment_setup_tree.heading('min_temp', text = 'Minimum Temperature (K)')
                self.experiment_setup_tree.heading('max_temp', text = 'Maximum Temperature (K)')
                self.experiment_setup_tree.heading('experiment_type', text = 'Experiment Type')
                self.experiment_setup_tree.heading('responsible_name', text = 'Responsible Name')
          
            
                # get the values related to the experiment setup table
                
                val = None
                user_name = str()
                for experiment_setup in res:
                    user_name_labid = database_utils.fetchall_query(connection, 'SELECT laboratory_id FROM user WHERE id = {}'.format(experiment_setup[9]))[0][0]
                    user_name = ' '.join([database_utils.fetchall_query(connection, 'SELECT firstname FROM user WHERE id = {}'.format(experiment_setup[9]))[0][0],
                                         database_utils.fetchall_query(connection, 'SELECT lastname FROM user WHERE id = {}'.format(experiment_setup[9]))[0][0],
                                         '(' + database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(user_name_labid))[0][0] + ')'])
                    #' ' + database_utils.fetchall_query(connection, 'SELECT lastname FROM user WHERE id = {}'.format(experiment_setup[9]))[0][0]
                    val = (experiment_setup[0],
                           experiment_setup[1],
                           experiment_setup[2],
                           experiment_setup[3],
                           experiment_setup[4],
                           experiment_setup[5],
                           experiment_setup[6],
                           experiment_setup[7],
                           database_utils.fetchall_query(connection, 'SELECT name FROM experiment_type WHERE id = {}'.format(experiment_setup[8]))[0][0],
                           user_name)
                    self.experiment_setup_tree.insert('',tk.END, values = val)

                self.experiment_setup_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(self, connection, 'experiment_setup', parent)
                GUI_utils.AddButton(self, connection, 'experiment_setup', parent)

                
            else:
                self.label_no_experiment_setup = tk.Label(self, text = 'There is no data in the experiment_setup table')
                self.label_no_experiment_setup.pack()    

                
        else:
            self.label_no_experiment_setup = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_experiment_setup.pack()

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
    
    widget.tab_experiment_setup = ExperimentSetupTree(widget.tabcontrol_experiment, connection)
    widget.tabcontrol_experiment.add(widget.tab_experiment_setup, text = 'Experiment Setup')
        
    widget.tabcontrol_experiment.pack(expand = 1, fill = 'both')