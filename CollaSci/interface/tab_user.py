'''
module to develop the user tab of the GUI
'''
import tkinter as tk
from tkinter import ttk

import CollaSci.db_function.database_utils as database_utils
import CollaSci.interface.GUI_utils as GUI_utils



class UserWidget(tk.Frame):
    def __init__(self, parent, connection):
        
        # define the frame for the user tab
        tk.Frame.__init__(self, parent)
        
        # define the first label holding the already defined users 
        self.label = tk.Label(self, text = 'Registered users', relief = 'ridge')
        self.label.pack()
        UserTree(self, connection)
        
class UserTree():
    def __init__(self, parent, connection): 
        
        # get a table with the connection 
        if connection is not None:
            # get the results from the user database
            
            res = database_utils.fetchall_query(connection, 'SELECT * FROM user')
            if res is not None:
                # define columns 
            
                user_col = ('id','firstname','lastname','status','laboratory')    
            
                # initiate treeview
                
                self.user_tree = ttk.Treeview(parent, columns = user_col, show = 'headings')
                
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
                
                GUI_utils.DeleteButton(parent, connection, 'user')

                
            else:
                self.label_no_user_data = tk.Label(parent, text = 'There is no data in the user table')
                self.label_no_user_data.pack()
        else:
            self.label_no_user_data = tk.Label(parent, text = 'There is no SQL connection')
            self.label_no_user_data.pack()
         