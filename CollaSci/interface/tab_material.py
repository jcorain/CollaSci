'''
module to develop the material tab of the GUI
'''
import tkinter as tk
from tkinter import ttk
import tkcalendar 
import datetime

import CollaSci.db_function.database_utils as database_utils
import CollaSci.db_function.tables_update as table_update

import CollaSci.interface.GUI_utils as GUI_utils

class MaterialWidget(tk.Frame):
    def __init__(self, parent, connection):
        
        # define the frame for the user tab
        tk.Frame.__init__(self, parent)
        create_material_tabs(self, connection)

class MaterialTypeTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        
        #  define the first label holding the already defined users 
        tk.Label(self, text = 'Registered material types', relief = 'ridge').pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM material_type')
            if res is not None:
                # define columns 
            
                col = ('id','name')    
                
                # initiate treeview
                
                self.material_type_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
                # define headings
                
                self.material_type_tree.heading('id', text = 'id')
                self.material_type_tree.heading('name', text = 'Name')
            
                # get the values related to the experiment type table
                
                val = None
                for material_type in res:
                    val = (material_type[0],
                           material_type[1])
                    self.material_type_tree.insert('',tk.END, values = val)

                self.material_type_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(self, connection, 'material_type', parent)
                GUI_utils.AddButton(self, connection, 'material_type', parent)
    
            else:
                tk.Label(self, text = 'There is no data in the material_type table').pack()
     
        else:
            tk.Label(self, text = 'There is no SQL connection').pack()
            

class MaterialTypeAdd():
    def __init__(self, popup, connection, grandparent):
       
        
        name_entry = GUI_utils.AddValueEntry(popup, connection, grandparent, 'Name')
        name = name_entry.value
        
        # add the add button 
        
        tk.Button(popup, 
                  text = 'Add material type column', 
                  command = lambda : add_material_type_col(popup, 
                                                           name, 
                                                           connection, 
                                                           grandparent)).pack()


class CompoundTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        
       #  define the first label holding the already defined users 
        self.label_compound = tk.Label(self, text = 'Registered compounds', relief = 'ridge')
        self.label_compound.pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM compound')
            if res is not None:
                # define columns 
            
                col = ('id','name', 'formula', 'material_type')    
                
                # initiate treeview
                
                self.compound_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
                # define headings
                
                self.compound_tree.heading('id', text = 'id')
                self.compound_tree.heading('name', text = 'Name')
                self.compound_tree.heading('formula', text = 'Formula')
                self.compound_tree.heading('material_type', text = 'Material Type')
            
                # get the values related to the experiment type table
                
                val = None
                for compound in res:
                    val = (compound[0],
                           compound[1],
                           compound[2],
                           database_utils.fetchall_query(connection, 'SELECT name FROM material_type WHERE id = {}'.format(compound[3]))[0][0])
                    self.compound_tree.insert('',tk.END, values = val)

                self.compound_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(self, connection, 'compound', parent)
                GUI_utils.AddButton(self, connection, 'compound', parent)

                
            else:
                self.label_no_matterial_type = tk.Label(self, text = 'There is no data in the compound table')
                self.label_no_compound.pack()    

                
        else:
            self.label_no_compound = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_compound.pack()
            
class CompoundAdd():
    def __init__(self, popup, connection, grandparent):
        
        # add the name values 
        
        self.name_lab = tk.Label(popup, text = 'Name')
        self.name_lab.pack(expand = 1, fill = 'both')
        name = tk.StringVar(popup)
        self.name_entry = tk.Entry(popup, textvariable = name)
        self.name_entry.pack(expand = 1, fill = 'both')
        
        # add the formula values 
        
        self.formula_lab = tk.Label(popup, text = 'Formula')
        self.formula_lab.pack(expand = 1, fill = 'both')
        formula = tk.StringVar(popup)
        self.formula_entry = tk.Entry(popup, textvariable = formula)
        self.formula_entry.pack(expand = 1, fill = 'both')
        
        # add the material type values 
                
        self.experiement_type_lab = tk.Label(popup, text = 'Material Type (if the material_type you want does not exist in the list please update the material_type table.')
        self.experiement_type_lab.pack(expand = 1, fill = 'both')
        material_type = tk.StringVar(popup)
        material_type_val = [val[0] for val in database_utils.fetchall_query(connection, 'SELECT name FROM material_type')]
        self.material_type_list = ttk.Combobox(popup, values = material_type_val, textvariable = material_type)
        self.material_type_list.set("Pick a Material Type")
        self.material_type_list.pack(expand = 1, fill = 'both')
        
        # add the add button 
        
        self.add_compound_button = tk.Button(popup, 
                                             text = 'Add compound column',
                                             command = lambda : add_compound_col(popup, name, formula, material_type, connection, grandparent))
        self.add_compound_button.pack()

class BatchTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        
       #  define the first label holding the already defined users 
        self.label_batch = tk.Label(self, text = 'Registered batches', relief = 'ridge')
        self.label_batch.pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM batch')
            if res is not None:
                # define columns 
            
                col = ('id','name', 'mass', 'colour', 'type', 'creation_date', 'compound_name', 'grower_name')    
                
                # initiate treeview
                
                self.batch_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
                # define headings
                
                self.batch_tree.heading('id', text = 'id')
                self.batch_tree.heading('name', text = 'Name')
                self.batch_tree.heading('mass', text = 'Mass (g)')
                self.batch_tree.heading('colour', text = 'Colour')
                self.batch_tree.heading('type', text = 'Crystal Type')
                self.batch_tree.heading('creation_date', text = 'Creation Date')
                self.batch_tree.heading('compound_name', text = 'Compound Name')
                self.batch_tree.heading('grower_name', text = 'Grower Name')
            
                # get the values related to the experiment type table
                                
                val = None
                grower_name = str()
                                               
                for batch in res:
                    
                    grower_name_labid = database_utils.fetchall_query(connection, 'SELECT laboratory_id FROM user WHERE id = {}'.format(batch[7]))[0][0]
                    grower_name = ' '.join([database_utils.fetchall_query(connection, 'SELECT firstname FROM user WHERE id = {}'.format(batch[7]))[0][0],
                                          database_utils.fetchall_query(connection, 'SELECT lastname FROM user WHERE id = {}'.format(batch[7]))[0][0],
                                          '(' + database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(grower_name_labid))[0][0] + ')'])
                    
                    val = (batch[0],
                           batch[1],
                           batch[2],
                           batch[3],
                           batch[4],
                           batch[5],
                           database_utils.fetchall_query(connection, 'SELECT name FROM compound WHERE id = {}'.format(batch[6]))[0][0],
                           grower_name)
                    self.batch_tree.insert('',tk.END, values = val)

                self.batch_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(self, connection, 'batch', parent)
                GUI_utils.AddButton(self, connection, 'batch', parent)

                
            else:
                self.label_no_matterial_type = tk.Label(self, text = 'There is no data in the batch table')
                self.label_no_batch.pack()    

                
        else:
            self.label_no_batch = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_batch.pack()

class BatchAdd():
    def __init__(self, popup, connection, grandparent):
        
        # add the name values 
        
        self.name_lab = tk.Label(popup, text = 'Name')
        self.name_lab.pack(expand = 1, fill = 'both')
        name = tk.StringVar(popup)
        self.name_entry = tk.Entry(popup, textvariable = name)
        self.name_entry.pack(expand = 1, fill = 'both')
        
        # add the mass values 
        
        self.mass_lab = tk.Label(popup, text = 'Mass (g)')
        self.mass_lab.pack(expand = 1, fill = 'both')
        mass = tk.StringVar(popup)
        self.mass_entry = tk.Entry(popup, textvariable = mass)
        self.mass_entry.pack(expand = 1, fill = 'both')
        
        # add the colour values 
        
        self.colour_lab = tk.Label(popup, text = 'Colour')
        self.colour_lab.pack(expand = 1, fill = 'both')
        colour = tk.StringVar(popup)
        self.colour_entry = tk.Entry(popup, textvariable = colour)
        self.colour_entry.pack(expand = 1, fill = 'both')
        
        # add the crystal type name values 
                
        self.crystal_type_lab = tk.Label(popup, text = 'Crystal Type')
        self.crystal_type_lab.pack(expand = 1, fill = 'both')
        crystal_type = tk.StringVar(popup)
        crystal_type_val = ['powder','polycristal','single cristal']
        self.crystal_type_list = ttk.Combobox(popup, values = crystal_type_val, textvariable = crystal_type)
        self.crystal_type_list.set("Pick a Crystal Type Name")
        self.crystal_type_list.pack(expand = 1, fill = 'both')
        
        # add the creation date value 
               
        self.creationdate_lab = tk.Label(popup, text = 'Batch creation date')
        self.creationdate_lab.pack()
        creationdate = tk.StringVar(popup, datetime.date.today().strftime('%d/%m/%Y'))
        self.creationdate_entry = tkcalendar.DateEntry(popup, textvariable = creationdate, date_pattern = 'dd/mm/yyyy')
        self.creationdate_entry.pack(expand = 1, fill = 'both')

        # add the compound name values 
                
        self.compound_name_lab = tk.Label(popup, text = 'Compound Name (if the compound_name you want does not exist in the list please update the compound table).')
        self.compound_name_lab.pack(expand = 1, fill = 'both')
        compound_name = tk.StringVar(popup)
        compound_name_val = [val[0] for val in database_utils.fetchall_query(connection, 'SELECT name FROM compound')]
        self.compound_name_list = ttk.Combobox(popup, values = compound_name_val, textvariable = compound_name)
        self.compound_name_list.set("Pick a Compound Name")
        self.compound_name_list.pack(expand = 1, fill = 'both')
        
        # add the responsible name values 
                
        self.grower_name_lab = tk.Label(popup, text = 'Grower name (if the grower_name you want does not exist in the list please update the user table).')
        self.grower_name_lab.pack(expand = 1, fill = 'both')
        grower_name = tk.StringVar(popup)     
        grower_name_val = [' '.join([val[0],val[1], '(' + database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(val[2]))[0][0] + ')']) for val in database_utils.fetchall_query(connection, 'SELECT firstname, lastname, laboratory_id FROM user')]
        self.grower_name_list = ttk.Combobox(popup, values = grower_name_val, textvariable = grower_name)
        self.grower_name_list.set("Pick a Grower Name")
        self.grower_name_list.pack(expand = 1, fill = 'both')
        
        # add the add button 
        
        self.add_batch_button = tk.Button(popup, 
                                              text = 'Add batch column',
                                              command = lambda : add_batch_col(popup, 
                                                                               name,
                                                                               mass, 
                                                                               colour, 
                                                                               crystal_type,
                                                                               creationdate,
                                                                               compound_name,
                                                                               grower_name,
                                                                               connection, 
                                                                               grandparent))
        self.add_batch_button.pack()




def add_material_type_col(popup, name, connection, grandparent):
    
    table_update.add_row_material_type_table(name.get(), connection)
    
    # update the user table 
    popup.destroy()

    GUI_utils.update_table('material_type', connection, grandparent)
    
def add_compound_col(popup, name, formula, material_type, connection, grandparent):
    
    # get the material type id 
    material_type_id = database_utils.fetchall_query(connection, 'SELECT id FROM material_type WHERE name = "{}"'.format(material_type.get()))[0][0]
    
    table_update.add_row_compound_table(name.get(), formula.get(), material_type_id, connection)
    
    # update the user table 
    popup.destroy()

    GUI_utils.update_table('compound', connection, grandparent)
    
def add_batch_col(popup, 
                  name,
                  mass, 
                  colour, 
                  crystal_type,
                  creationdate,
                  compound_name,
                  grower_name,
                  connection, 
                  grandparent):
    
    # get the compound id 
    compound_id = database_utils.fetchall_query(connection, 'SELECT id FROM compound WHERE name = "{}"'.format(compound_name.get()))[0][0]
    
    # get the laboratory id from responsible name 
    
    laboratory_id = database_utils.fetchall_query(connection, 'SELECT id FROM laboratory WHERE name = "{}"'.format(grower_name.get().split('(')[1].split(')')[0]))[0][0]
    grower_id = database_utils.fetchall_query(connection, 'SELECT id FROM user WHERE firstname = "{}" AND lastname = "{}" AND laboratory_id = {}'.format(grower_name.get().split(' ')[0], grower_name.get().split(' ')[1], laboratory_id))[0][0]

    table_update.add_row_batch_table(name.get(),
                                     mass.get(),
                                     colour.get(), 
                                     crystal_type.get(), 
                                     creationdate.get(),
                                     compound_id, 
                                     grower_id, 
                                     connection)
    
    # update the user table 
    popup.destroy()
    
    GUI_utils.update_table('compound', connection, grandparent)

def create_material_tabs(widget, connection):     
    # define the new tabs with user, status, laboratory and university 
    widget.tabcontrol_material = ttk.Notebook(widget)
    
    widget.tab_material_type = MaterialTypeTree(widget.tabcontrol_material, connection)
    widget.tabcontrol_material.add(widget.tab_material_type, text = 'Material Type')
    
    widget.tab_compound = CompoundTree(widget.tabcontrol_material, connection)
    widget.tabcontrol_material.add(widget.tab_compound, text = 'Compound')
    
    widget.tab_batch = BatchTree(widget.tabcontrol_material, connection)
    widget.tabcontrol_material.add(widget.tab_batch, text = 'Batch')
        
    widget.tabcontrol_material.pack(expand = 1, fill = 'both')