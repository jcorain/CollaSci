# -*- coding: utf-8 -*-
"""
module for GUI utils
"""
import tkinter as tk

import CollaSci.db_function.database_utils as database_utils
import CollaSci.interface.tab_user as tab_user

def delete_popup(parent, connection, table_name):
    
    # define the popup window
    
    popup = tk.Toplevel()
    popup.title('Delete a column')
    
    # get the label
    
    del_label = tk.Label(popup, text = 'Column id to delete')
    del_label.pack()
    
    # define the first string value 
    
    mystring = tk.StringVar(popup)
    
    # get the entry for col number 
    
    id_entry = tk.Entry(popup, textvariable = mystring)
    id_entry.pack()
    
    # define the callback from button 
    
    def delete_col(parent, connection, table_name):
        
        # get thepossible id values to delete 
        
        existing_id = []
        existing_id_tup = database_utils.fetchall_query(connection, 'SELECT id FROM {}'.format(table_name))
        for val in existing_id_tup:
            existing_id = existing_id + [str(val[0])]

        # if the id to delete is in the possible value delete it 
        # else get a warning message

        if mystring.get() in existing_id:
            confirmation = tk.messagebox.askokcancel('','The colum id number {} is going to be deleted.'.format(mystring.get()))
            if confirmation:
                database_utils.delete_id_from_table(connection, table_name, int(mystring.get()))
                
                # to updtae the treeview, delete it and then redo it 
                
                for widget in parent.winfo_children():
                    # delete delete button
                    if '!button' in str(widget):
                        widget.destroy()
                    
                    # delte treview and recreate it 
                    if 'treeview' in str(widget):
                        widget.destroy()
                        if table_name == 'user':
                            tab_user.UserTree(parent, connection)                
            
        else:
            tk.messagebox.showinfo('','The colum id number {} does not exist. Please select another id value.'.format(mystring.get()))
            
        popup.destroy()
        
        
    
    ok_button = tk.Button(popup, text = 'Delete column', command = lambda : delete_col(parent, connection, table_name))
    ok_button.pack()


class DeleteButton(tk.Frame):
    def __init__(self, parent, connection, table_name):
        
        # define the frame for the delete buttton
        tk.Frame.__init__(self, parent)
        
        # define the first label holding the already defined users 
        
        self.label_del = tk.Button(parent, text = 'Delete a column', command = lambda : delete_popup(parent, connection, table_name))
        self.label_del.pack()