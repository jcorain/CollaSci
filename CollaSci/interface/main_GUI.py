'''module to create the main interface of the gui'''

from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import tkinter as tk
from tkinter import ttk 

import os  

import CollaSci.db_function.database_utils as database_utils
import CollaSci.db_function.tables_update as tables_update

import CollaSci.interface.tab_user as tab_user


# create the dummy db 

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
name = 'database_test.sqlite'


# if the database exists delete it 

if os.path.exists(os.path.join(path, name)):
    os.remove(os.path.join(path, name))

connection = database_utils.create_or_connect_db(path, name)

database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")

# create the first university row

university_name = 'Université Paris Saclay'
university_country = 'France'
university_city = 'Gif-sur-Yvette'
university_address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
tables_update.add_row_university_table(university_name, university_country, university_city, university_address, connection)

# create the second university row

university_name = 'Paul Scherrer Institute'
university_country = "Switzerland"
university_city = 'Villigen'
university_address = 'PSI CH, Forschungsstrasse 111, 5232 Villigen'
tables_update.add_row_university_table(university_name, university_country, university_city, university_address, connection)

# create the first laboratory row 

laboratory_name = 'Laboratoire de Physique des Solides'
university_id = 1
tables_update.add_row_laboratory_table(laboratory_name, university_id, connection)

# create the second laboratory row 

laboratory_name = 'Laboratoire de Physique Théoriques et de Modèles Statistiques'
university_id = 1
tables_update.add_row_laboratory_table(laboratory_name, university_id, connection)

# create the third laboratory row 

laboratory_name = 'Laboratory for Muon Spin Spectroscopy'
university_id = 2
tables_update.add_row_laboratory_table(laboratory_name, university_id, connection)

# create the first status row 

status_name = 'PhD Student'
tables_update.add_row_status_table(status_name, connection)

# create the second status row 

status_name = 'Postdoc'
tables_update.add_row_status_table(status_name, connection)

# create the first material_type row 

material_type_name = 'Quantum Spin Liquid'
tables_update.add_row_material_type_table(material_type_name, connection)

# create the second material_type row

material_type_name = 'Superconductor'
tables_update.add_row_material_type_table(material_type_name, connection)

# create the first compound row

compound_name = 'DQVOF'
compound_formula = '(NH4)2[C7H14N][V7O6F18]'
material_type_id = 1
tables_update.add_row_compound_table(compound_name, compound_formula, material_type_id, connection)

# create the second compound row

compound_name = 'Herbertsmithite'
compound_formula = 'ZnCu3(OH)6Cl2'
material_type_id = 1
tables_update.add_row_compound_table(compound_name, compound_formula, material_type_id, connection)

# create the third compound row

compound_name = 'YBACUO'
compound_formula = 'YBa2Cu3O7'
material_type_id = 2
tables_update.add_row_compound_table(compound_name, compound_formula, material_type_id, connection)

# create the first experiment_type row

experiment_type_name = 'Heat Capacity vs Temperature'
tables_update.add_row_experiment_type_table(experiment_type_name, connection)

# create the second experiment_type row

experiment_type_name = 'Magnetization vs Temperature'
tables_update.add_row_experiment_type_table(experiment_type_name, connection)

# create the first user row

user_firstname = 'Jean-Christophe'
user_lastname = 'Orain'
status_id = 1
laboratory_id = 1
tables_update.add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)

# create the second user row

user_firstname = 'Jean-Christophe'
user_lastname = 'Orain'
status_id = 2
laboratory_id = 3
tables_update.add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)

# create the third user row

user_firstname = 'Gediminas'
user_lastname = 'Simutis'
status_id = 2
laboratory_id = 3
tables_update.add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)

# create the first experimental_setup row

experimental_setup_name = 'MMPS He4'
roomname = 'Salon'
experimental_setup_start_date = '25/05/2018'
min_field = 0
max_field = 5
min_temperature = 1.5
max_temperature = 300
experiment_type_id = 1
responsible_id = 1
tables_update.add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)

# create the second experimental_setup row

experimental_setup_name = 'MMPS He4 bis'
roomname = 'Salon'
experimental_setup_start_date = '25/05/2018'
min_field = None
max_field = None
min_temperature = None
max_temperature = None
experiment_type_id = 1
responsible_id = 2
tables_update.add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
 
# create the first batch row
batch_name = "DQVOF 1"
mass = 100
color = 'green'
Type = "powder"
creation_date = '2019-10-12'
compound_id = 1
grower_id = 1
tables_update.add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)

# create the second batch row
batch_name = "Test 2002"
mass = 200
color = 'green'
Type = "single cristal"
creation_date = '2017-10-12'
compound_id = 2
grower_id = 3
tables_update.add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)

# create the first project row
project_name = "Super project"
project_responsible_id = 1
tables_update.add_row_project_table(project_name, project_responsible_id, connection)

# create the second project row
project_name = "Super other project"
project_responsible_id = 3
tables_update.add_row_project_table(project_name, project_responsible_id, connection)

# create the first data row

mass = 100
experiment_no = 1
field = 2 
temperature = 300 
date = '2018-01-21'
path_import = os.path.join(os.path.dirname(os.path.dirname(__file__)),'tests','data','PyzVOFZFCFC1T.dc.dat')
comment = None
experiment_setup_id = 1
user_id = 1
batch_id = 1
project_id = 1
    
tables_update.add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                      experiment_setup_id, user_id, batch_id, project_id, connection)

# create the second data row

mass = 150
experiment_no = 5
field = None 
temperature = None 
date = '2018-12-21'
path_import = os.path.join(os.path.dirname(os.path.dirname(__file__)),'tests','data','PyzVOFZFCFC0p1T.dc.dat')
comment = None
experiment_setup_id = 2
user_id = 3
batch_id = 1
project_id = 2

tables_update.add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                      experiment_setup_id, user_id, batch_id, project_id, connection)

connection.close()


def destroy_previous_widget():
    for widget in root.winfo_children():
        if str(widget) != '.!menu':
            widget.destroy()

def open_database_widget(data):
    
    dbframe = tk.Frame(root)
    
    if data is not None:
        db_path = os.path.dirname(data.name)
        db_name = os.path.basename(data.name)
        connection = database_utils.create_or_connect_db(db_path, db_name)
        dbname = tk.Label(dbframe, text = 'Loaded database : {}'.format(db_name), bd = 20)
    else:
        connection = None
        db_name = None
        dbname = tk.Label(dbframe, text = 'There is no connection to an sql database.', bd = 20)
    
    # set the database name 
    
    dbframe.pack()
    dbname.pack()
    
    # create the tabs
    
    create_tabs(connection, db_name)

def create_tabs(connection, db_name):
    
    if connection is not None:
    # create the tabControl
        tabframe = tk.Frame(root)
        tabControl = ttk.Notebook(tabframe)
        
        # create the tabs 
        
        user_tab = tab_user.UserWidget(tabControl, connection, db_name)
        tabControl.add(user_tab, text = 'User')
        
        tab_experiment = ttk.Frame(tabControl)
        tabControl.add(tab_experiment, text = 'Experiment')
        
        tab_material = ttk.Frame(tabControl)
        tabControl.add(tab_material, text = 'Material')
        
        tab_project = ttk.Frame(tabControl)
        tabControl.add(tab_project, text = 'Project')
        
        tab_data = ttk.Frame(tabControl)
        tabControl.add(tab_data, text = 'Data')
        
        tabframe.pack(side = 'left', fill = 'both', expand = 1)
        tabControl.pack(expand = 1, fill = 'both')
    
# create the field to upload the database 

def LoadDb():
  
    # destroy the already existing widgets 
    destroy_previous_widget()
    
    # get the data 
    data = askopenfile(filetypes = [('database', '*.sqlite')])
    
    # open the connection to the database 
    
    open_database_widget(data)
    

def NewDb():
    
    # destroy the already existing widgets 
    destroy_previous_widget()
    
    # save the new data 
    
    data = asksaveasfile(filetypes = [('database', '*.sqlite')])
    
    # open the connection to the database 
    open_database_widget(data)


# create the root application 

root = tk.Tk()
root.title("CollaSci")

menu = tk.Menu(root)
root.config(menu = menu)
dbmenu = tk.Menu(menu, tearoff = False)
menu.add_cascade(label = 'DataBase', menu = dbmenu)
dbmenu.add_command(label = 'New database', command = NewDb)
dbmenu.add_command(label = 'Load database', command = LoadDb)

root.mainloop()

