'''
module to develop the user tab of the GUI
'''
import tkinter as tk
from tkinter import ttk

import CollaSci.db_function.database_utils as database_utils
# set the database path 

def delete_popup(connection, table_name):
    
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
    
    def delete_col(connection, table_name):
        
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
            
        else:
            tk.messagebox.showinfo('','The colum id number {} does not exist. Please select another id value.'.format(mystring.get()))
            
        popup.destroy()
        
    
    ok_button = tk.Button(popup, text = 'Delete column', command = lambda : delete_col(connection, table_name))
    ok_button.pack()


class DeleteButton(tk.Frame):
    def __init__(self, parent, connection, table_name):
        
        # # define the frame for the delete buttton
        tk.Frame.__init__(self, parent)
        
        # define the first label holding the already defined users 
        
        self.label_del = tk.Button(parent, text = 'Delete a column', command = lambda : delete_popup(connection, table_name))
        self.label_del.pack()

class UserWidget(tk.Frame):
    def __init__(self, parent, connection, db_name):
        
        # define the frame for the user tab
        tk.Frame.__init__(self, parent)
        
        # define the first label holding the already defined users 
        self.label = tk.Label(self, text = 'Registered users', relief = 'ridge')
        self.label.pack()
        
        # get a table with the connection 
        
        if connection is not None:
            
            # get the results from the user database
            
            res = database_utils.fetchall_query(connection, 'SELECT * FROM user')
            
            if res is not None:
                # define columns 
            
                user_col = ('id','firstname','lastname','status','laboratory')    
            
                # initiate treeview
                
                self.user_tree = ttk.Treeview(self, columns = user_col, show = 'headings')
                
                # define headings
                
                self.user_tree.heading('id', text = 'id')
                self.user_tree.heading('firstname', text = 'First Name')
                self.user_tree.heading('lastname', text = 'Last Name')
                self.user_tree.heading('status', text = 'Status')
                self.user_tree.heading('laboratory', text = 'Laboratory')
                
                
    
                # get the values related to the user table
                
                val = None
                
                for user in res:
                    val = (user[0],
                           user[1],
                           user[2],
                           database_utils.fetchall_query(connection, 'SELECT name FROM status WHERE id = {}'.format(user[3]))[0][0],
                           database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(user[4]))[0][0])
                 
                    self.user_tree.insert('',tk.END, values = val)
                    
                self.user_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                DeleteButton(self, connection, 'user')

                
            else:
                self.label_no_user_data = tk.Label(self, text = 'There is no data in the user table')
                self.label_no_user_data.pack()
            