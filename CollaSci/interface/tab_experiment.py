'''
module to develop the experiment tab of the GUI
'''
import tkinter as tk
from tkinter import ttk
import tkcalendar 
import datetime

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
        self.name_lab.pack(expand = 1, fill = 'both')
        
        # define the firstname string value 
        
        name = tk.StringVar(popup)
        
        # get the entry for firstname 
       
        self.name_entry = tk.Entry(popup, textvariable = name)
        self.name_entry.pack(expand = 1, fill = 'both')
                
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
            
class ExperimentSetupAdd():
    def __init__(self, popup, connection, grandparent):
        # add the first name values 
        self.name_lab = tk.Label(popup, text = 'Name')
        self.name_lab.pack(expand = 1, fill = 'both')
        
        # define the firstname string value 
        
        name = tk.StringVar(popup)
        
        # get the entry for firstname 
       
        self.name_entry = tk.Entry(popup, textvariable = name)
        self.name_entry.pack(expand = 1, fill = 'both')
        
        # add the room name values 
        self.roomname_lab = tk.Label(popup, text = 'Room Name')
        self.roomname_lab.pack()
        roomname = tk.StringVar(popup)
        self.roomname_entry = tk.Entry(popup, textvariable = roomname)
        self.roomname_entry.pack(expand = 1, fill = 'both')
                
        # add the start date value 
        
        self.startdate_lab = tk.Label(popup, text = 'Experiment start date')
        self.startdate_lab.pack()
        startdate = tk.StringVar(popup, datetime.date.today().strftime('%d/%m/%Y'))
        self.startdate_entry = tkcalendar.DateEntry(popup, textvariable = startdate, date_pattern = 'dd/mm/yyyy')
        self.startdate_entry.pack(expand = 1, fill = 'both')
        
        # add the min field values 
        self.minfield_lab = tk.Label(popup, text = 'Minimum Field (T)')
        self.minfield_lab.pack(expand = 1, fill = 'both')
        minfield = tk.StringVar(popup, None)
        self.minfield_entry = tk.Entry(popup, textvariable = minfield)
        self.minfield_entry.pack(expand = 1, fill = 'both')
        
        # add the max field values 
        self.maxfield_lab = tk.Label(popup, text = 'Maximum Field (T)')
        self.maxfield_lab.pack(expand = 1, fill = 'both')
        maxfield = tk.StringVar(popup, None)
        self.maxfield_entry = tk.Entry(popup, textvariable = maxfield)
        self.maxfield_entry.pack(expand = 1, fill = 'both')
    
        # add the min temperature values 
        self.mintemperature_lab = tk.Label(popup, text = 'Minimum Temperature (K)')
        self.mintemperature_lab.pack(expand = 1, fill = 'both')
        mintemperature = tk.StringVar(popup, None)
        self.mintemperature_entry = tk.Entry(popup, textvariable = mintemperature)
        self.mintemperature_entry.pack(expand = 1, fill = 'both')
        
        # add the max temperature values 
        self.maxtemperature_lab = tk.Label(popup, text = 'Maximum Temperature (K)')
        self.maxtemperature_lab.pack(expand = 1, fill = 'both')
        maxtemperature = tk.StringVar(popup, None)
        self.maxtemperature_entry = tk.Entry(popup, textvariable = maxtemperature)
        self.maxtemperature_entry.pack(expand = 1, fill = 'both')
    
        # add the experiment type values 
        
        self.experiement_type_lab = tk.Label(popup, text = 'Experiment Type (if the experiment_type you want does not exist in the list please update the experiment_type table.')
        self.experiement_type_lab.pack(expand = 1, fill = 'both')
        
        #define the status string value 
       
        experiment_type = tk.StringVar(popup)
        
        # get the list of existing status 
        experiment_type_val = [val[0] for val in database_utils.fetchall_query(connection, 'SELECT name FROM experiment_type')]
 
        self.experiment_typelist = ttk.Combobox(popup, values = experiment_type_val, textvariable = experiment_type)
        self.experiment_typelist.set("Pick a Experiment Type")
        self.experiment_typelist.pack(expand = 1, fill = 'both')
        
        # add the responsible name values 
        
        self.experiement_type_lab = tk.Label(popup, text = 'Responsible name (if the responsible_name you want does not exist in the list please update the user table.')
        self.experiement_type_lab.pack(expand = 1, fill = 'both')
        responsible_name = tk.StringVar(popup)
        
        responsible_name_val = [' '.join([val[0],val[1], '(' + database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(val[2]))[0][0] + ')']) for val in database_utils.fetchall_query(connection, 'SELECT firstname, lastname, laboratory_id FROM user')]
 
        self.responsible_namelist = ttk.Combobox(popup, values = responsible_name_val, textvariable = responsible_name)
        self.responsible_namelist.set("Pick a Responsible Name")
        self.responsible_namelist.pack(expand = 1, fill = 'both')
    
        # add the add button 
        
        self.add_user_button = tk.Button(popup, text = 'Add experiment setup column', command = lambda : add_experiment_setup_col(popup, name, roomname, startdate, 
                                                                                                                                  minfield, maxfield, mintemperature, maxtemperature,
                                                                                                                                  experiment_type, responsible_name,
                                                                                                                                  connection, grandparent))
        self.add_user_button.pack()


def add_experiment_type_col(popup, name, connection, grandparent):
    
    table_update.add_row_experiment_type_table(name.get(), connection)
    
    # update the user table 
    popup.destroy()

    GUI_utils.update_table('user', connection, grandparent)
    
def add_experiment_setup_col(popup, name, room_name, start_date, 
                             min_field, max_field, min_temperature, max_temperature,
                             experiment_type, responsible_name,
                             connection, grandparent):
    
    # get the experiment type id 
    experiment_type_id = database_utils.fetchall_query(connection, 'SELECT id FROM experiment_type WHERE name = "{}"'.format(experiment_type.get()))[0][0]
    
    # get the laboratory id from responsible name 
    
    laboratory_id = database_utils.fetchall_query(connection, 'SELECT id FROM laboratory WHERE name = "{}"'.format(responsible_name.get().split('(')[1].split(')')[0]))[0][0]
    responsible_id = database_utils.fetchall_query(connection, 'SELECT id FROM user WHERE firstname = "{}" AND lastname = "{}" AND laboratory_id = {}'.format(responsible_name.get().split(' ')[0], responsible_name.get().split(' ')[1], laboratory_id))[0][0]
    
    # set balnk field an temperature to None
    
    if min_field.get() == '':
        min_field = None
    else:
        min_field = min_field.get()
    if max_field.get() == '':
        max_field = None
    else:
        max_field = max_field.get()
    if min_temperature.get() == '':
        min_temperature = None
    else:
        min_temperature = min_temperature.get()
    if max_temperature.get() == '':
        max_temperature = None
    else:
        max_temperature = max_temperature.get()
   
        
    
    table_update.add_row_experiment_setup_table(name.get(), 
                                                room_name.get(), 
                                                start_date.get(), 
                                                min_field, 
                                                max_field,
                                                min_temperature, 
                                                max_temperature, 
                                                experiment_type_id,
                                                responsible_id, 
                                                connection)
  
    
    # update the user table 
    popup.destroy()

    GUI_utils.update_table('experiment_setup', connection, grandparent)



def create_experiment_tabs(widget, connection):     
    # define the new tabs with user, status, laboratory and university 
    widget.tabcontrol_experiment = ttk.Notebook(widget)
    
    widget.tab_experiment_type = ExperimentTypeTree(widget.tabcontrol_experiment, connection)
    widget.tabcontrol_experiment.add(widget.tab_experiment_type, text = 'Experiment Type')
    
    widget.tab_experiment_setup = ExperimentSetupTree(widget.tabcontrol_experiment, connection)
    widget.tabcontrol_experiment.add(widget.tab_experiment_setup, text = 'Experiment Setup')
        
    widget.tabcontrol_experiment.pack(expand = 1, fill = 'both')