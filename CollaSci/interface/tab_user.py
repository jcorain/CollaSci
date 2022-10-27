'''
module to develop the user tab of the GUI
'''
import tkinter as tk
from tkinter import ttk

import CollaSci.db_function.database_utils as database_utils
import CollaSci.db_function.tables_update as table_update
import CollaSci.interface.GUI_utils as GUI_utils

class UserWidget(tk.Frame):
    def __init__(self, parent, connection):
        
        # define the frame for the user tab
        tk.Frame.__init__(self, parent)
        create_user_tabs(self, connection)

def create_user_tabs(widget, connection):     
    # define the new tabs with user, status, laboratory and university 
    widget.tabcontrol_user = ttk.Notebook(widget)
    
    widget.tab_user = UserTree(widget.tabcontrol_user, connection)
    widget.tabcontrol_user.add(widget.tab_user, text = 'User')
    
    
    # self.tab_status = StatusTree(self.tabcontrol_user, connection)
    # self.tabcontrol_user.add(self.tab_status, text = 'Status')
    
    widget.tabcontrol_user.pack(expand = 1, fill = 'both')
    
class UserTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM user')
            if res is not None:
                # define columns 
            
                col = ('id','firstname','lastname','status','laboratory')    
            
                # define the first label holding the already defined users 
                self.label_user = tk.Label(self, text = 'Registered users', relief = 'ridge')
                self.label_user.pack()
                # initiate treeview
                
                self.user_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
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
                
                GUI_utils.DeleteButton(self, connection, 'user', parent)
                GUI_utils.AddButton(self, connection, 'user')

                
            else:
                self.label_no_user_data = tk.Label(self, text = 'There is no data in the user table')
                self.label_no_user_data.pack()
        else:
            self.label_no_user_data = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_user_data.pack()
            
class UserAdd():
    def __init__(self, parent, connection, grandparent):
        if connection is not None:
            # add the first name values 
            self.firstname = tk.Label(parent, text = 'First Name')
            self.firstname.pack()
            
            # define the firstname string value 
            
            firstname = tk.StringVar(parent)
            
            # get the entry for firstname 
           
            self.firstname_entry = tk.Entry(parent, textvariable = firstname)
            self.firstname_entry.pack()
            
            # add the first name values 
            self.lastname = tk.Label(parent, text = 'Last Name')
            self.lastname.pack()
            
            #define the firstname string value 
           
            lastname = tk.StringVar(parent)
            
            # get the entry for lastname 
           
            self.lastname_entry = tk.Entry(parent, textvariable = lastname)
            self.lastname_entry.pack()
            
            # add the status values 
            
            self.status = tk.Label(parent, text = 'Status (if the status you want does not exist in the list please update the status table.')
            self.status.pack()
            
            #define the status string value 
           
            status = tk.StringVar(parent)
            
            # get the list of existing status 
            status_val = [val[0] for val in database_utils.fetchall_query(connection, 'SELECT name FROM status')]
 
            self.statuslist = ttk.Combobox(parent, values = status_val, textvariable = status)
            self.statuslist.set("Pick a status")
            self.statuslist.pack()
            
            # add the laboratory values 
            
            self.laboratory = tk.Label(parent, text = 'Laboratory (if the laboratory you want does not exist in the list please update the laboratory table.')
            self.laboratory.pack()
            
            #define the laboratory string value 
           
            laboratory = tk.StringVar(parent)
            # get the list of existing status 
            laboratory_val = [val[0] for val in database_utils.fetchall_query(connection, 'SELECT name FROM laboratory')]
 
            self.laboratorylist = ttk.Combobox(parent, values = laboratory_val, textvariable = laboratory)
            self.laboratorylist.set("Pick a laboratory")
            self.laboratorylist.pack()
            
            # add the add button 
            
            self.add_button = tk.Button(parent, text = 'Add user column', command = lambda : add_user_col(parent, firstname, lastname, status, laboratory, connection, grandparent))
            self.add_button.pack()
        
def add_user_col(parent, firstname, lastname, status, laboratory, connection, grandparent):
    
    # get the status id 
    status_id = database_utils.fetchall_query(connection, 'SELECT id FROM status WHERE name = "{}"'.format(status.get()))[0][0]
    
    # get the laboratory id 
    
    laboratory_id = database_utils.fetchall_query(connection, 'SELECT id FROM laboratory WHERE name = "{}"'.format(laboratory.get()))[0][0]
    
    table_update.add_row_user_table(firstname.get(), lastname.get(), status_id, laboratory_id, connection)
    
    # update the user table 
    
    GUI_utils.update_table(grandparent, 'user', connection)
    parent.destroy()


class StatusTree(tk.Frame):
    def __init__(self, parent, connection): 
        
        tk.Frame.__init__(self, parent)
        
        # get a table with the connection 
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM status')
            if res is not None:
                # define columns 
            
                col = ('id','name')    
            
                # define the first label holding the already defined users 
                self.label_status = tk.Label(self, text = 'Registered status', relief = 'ridge')
                self.label_status.pack()
            
                # initiate treeview
                
                self.status_tree = ttk.Treeview(parent, columns = col, show = 'headings')
                
                # define headings
                
                self.status_tree.heading('id', text = 'id')
                self.status_tree.heading('name', text = 'Name')                
                
    
                # get the values related to the user table
                
                val = None
                
                for value in res:
                    val = (value[0],
                           value[1]) 
                    self.status_tree.insert('',tk.END, values = val)

                self.status_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(parent, connection, 'status')
                GUI_utils.AddButton(parent, connection, 'status')

                
            else:
                self.label_no_status_data = tk.Label(parent, text = 'There is no data in the status table')
                self.label_no_status_data.pack()
        else:
            self.label_no_status_data = tk.Label(parent, text = 'There is no SQL connection')
            self.label_no_status_data.pack()
            
class StatusAdd():
    def __init__(self, parent, connection, grandparent):
        if connection is not None:
            # add the first name values 
            self.statusname = tk.Label(parent, text = 'Name')
            self.statusname.pack()
            
            # define the firstname string value 
            
            statusname = tk.StringVar(parent)
            
            # get the entry for firstname 
           
            self.statusname_entry = tk.Entry(parent, textvariable = statusname)
            self.statusname_entry.pack()
            
        
            
            # add the add button 
            
            self.status_add_button = tk.Button(parent, text = 'Add status column', command = lambda : add_status_col(parent, statusname, connection, grandparent))
            self.status_add_button.pack()
        
def add_status_col(parent, name, connection, grandparent):
        
    table_update.add_row_status_table(name.get(), connection)
    
    # update the user table 
    
    GUI_utils.update_table(grandparent, 'status', connection)
    parent.destroy()
