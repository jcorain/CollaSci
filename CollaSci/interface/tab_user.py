'''
module to develop the user tab of the GUI
'''
import tkinter as tk

import CollaSci.db_function.database_utils as database_utils
# set the database path 

class UserWidget(tk.Frame):
    def __init__(self, parent, connection, db_name):
        
        # define the frame for the user tab
        tk.Frame.__init__(self, parent)
        
        # define the first label holding the already defined users 
        self.label = tk.Label(self, text = 'Registered users')
        self.label.pack(side = 'left')
        
        # get a table with the connection 
        
        if connection is not None:
            # get the values related to the user table
            res = database_utils.fetchall_query(connection, 'SELECT * FROM user')
            firstnames = []
            lastnames = []
            laboratory_names = []
            
            for user in res:
                firstnames = firstnames + [user[1]]
                lastnames = lastnames + [user[2]]
                
                laboratory_names =laboratory_names + [user[4]]