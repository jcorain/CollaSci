# -*- coding: utf-8 -*-
"""
module for GUI utils
"""
import tkinter as tk

import CollaSci.db_function.database_utils as database_utils
import CollaSci.interface.tab_user as tab_user
import CollaSci.interface.tab_experiment as tab_experiment


def delete_popup(connection, table_name, grandparent):
    
    # define the popup window
        
    popup = tk.Toplevel()
    popup.title('Delete a column')
    
    # get the label
    
    del_label = tk.Label(popup, text = 'Column id to delete')
    del_label.pack()
    
    # define the first string value 
    
    id_val = tk.StringVar(popup)
    
    # get the entry for col number 
    
    id_entry = tk.Entry(popup, textvariable = id_val)
    id_entry.pack()
    
    # define the callback from button 
    
    def delete_col(connection, table_name, grandparent):
                
        # get thepossible id values to delete 
        existing_id = []
        existing_id_tup = database_utils.fetchall_query(connection, 'SELECT id FROM {}'.format(table_name))
        for val in existing_id_tup:
            existing_id = existing_id + [str(val[0])]

        # if the id to delete is in the possible value delete it 
        # else get a warning message

        if id_val.get() in existing_id:
            confirmation = tk.messagebox.askokcancel('','The colum id number {} is going to be deleted.'.format(id_val.get()))
            if confirmation:
                database_utils.delete_id_from_table(connection, table_name, int(id_val.get()))
                update_table(table_name, connection, grandparent)
        else:
            tk.messagebox.showinfo('','The colum id number {} does not exist. Please select another id value.'.format(id_val.get()))
            
        popup.destroy()
        
    ok_button = tk.Button(popup, text = 'Delete column', command = lambda : delete_col(connection, table_name, grandparent))
    ok_button.pack()
    
def add_popup(connection, table_name, grandparent):
    
    # define the popup window
    
    popup = tk.Toplevel()
    popup.title('Add a column')
    
    if table_name == 'user':
        tab_user.UserAdd(popup, connection, grandparent)
    elif table_name == 'status':
        tab_user.StatusAdd(popup, connection, grandparent)
    elif table_name == 'university':
        tab_user.UniversityAdd(popup, connection, grandparent)
    elif table_name == 'laboratory':
        tab_user.LaboratoryAdd(popup, connection, grandparent)
    elif table_name == 'experiment_type':
        tab_experiment.ExperimentTypeAdd(popup, connection, grandparent)
    
        
    
        
def update_table(table_name, connection, grandparents):
    # to update the table, delete it and then redo it
    if type(grandparents) is not list:
        grandparents = [grandparents]
    for grandparent in grandparents:
        for widget in grandparent.winfo_children():
            widget.destroy()
        if table_name == 'user':
            tab_user.create_user_tabs(grandparent, connection)
            tab_experiment.create_experiment_tabs(grandparent, connection)
        if table_name in ['user', 'status', 'university', 'laboratory']:
            tab_user.create_user_tabs(grandparent, connection)
        elif table_name in ['experiment_type', 'experiment_setup']:
            tab_experiment.create_experiment_tabs(grandparent, connection)
            

class DeleteButton():
    def __init__(self, parent, connection, table_name, grandparent):                
        self.del_button = tk.Button(parent, text = 'Delete a column', command = lambda : delete_popup(connection, table_name, grandparent))
        self.del_button.pack()
        
class AddButton():
    def __init__(self, parent, connection, table_name, grandparent):
        self.add_button = tk.Button(parent, text = 'Add a column', command = lambda : add_popup(connection, table_name, grandparent))
        self.add_button.pack()