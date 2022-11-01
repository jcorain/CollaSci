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
    
class UserTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        
       #  define the first label holding the already defined users 
        self.label_user = tk.Label(self, text = 'Registered users', relief = 'ridge')
        self.label_user.pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM user')
            if res is not None:
                # define columns 
            
                col = ('id','firstname','lastname','status','laboratory')    
                
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
                GUI_utils.AddButton(self, connection, 'user', parent)

                
            else:
                self.label_no_user = tk.Label(self, text = 'There is no data in the user table')
                self.label_no_user.pack()    

                
        else:
            self.label_no_user = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_user.pack()    

       
       
class UserAdd():
    def __init__(self, popup, connection, grandparent):
        # add the first name values 
        self.firstname_lab = tk.Label(popup, text = 'First Name')
        self.firstname_lab.pack()
        
        # define the firstname string value 
        
        firstname = tk.StringVar(popup)
        
        # get the entry for firstname 
       
        self.firstname_entry = tk.Entry(popup, textvariable = firstname)
        self.firstname_entry.pack()
        
        # add the first name values 
        self.lastname_lab = tk.Label(popup, text = 'Last Name')
        self.lastname_lab.pack()
        
        #define the firstname string value 
       
        lastname = tk.StringVar(popup)
        
        # get the entry for lastname 
       
        self.lastname_entry = tk.Entry(popup, textvariable = lastname)
        self.lastname_entry.pack()
        
        # add the status values 
        
        self.status_lab = tk.Label(popup, text = 'Status (if the status you want does not exist in the list please update the status table.')
        self.status_lab.pack()
        
        #define the status string value 
       
        status = tk.StringVar(popup)
        
        # get the list of existing status 
        status_val = [val[0] for val in database_utils.fetchall_query(connection, 'SELECT name FROM status')]
 
        self.statuslist = ttk.Combobox(popup, values = status_val, textvariable = status)
        self.statuslist.set("Pick a status")
        self.statuslist.pack()
        
        # add the laboratory values 
        
        self.laboratory_lab = tk.Label(popup, text = 'Laboratory (if the laboratory you want does not exist in the list please update the laboratory table.')
        self.laboratory_lab.pack()
        
        #define the laboratory string value 
       
        laboratory = tk.StringVar(popup)
        # get the list of existing status 
        laboratory_val = [val[0] for val in database_utils.fetchall_query(connection, 'SELECT name FROM laboratory')]
 
        self.laboratorylist = ttk.Combobox(popup, values = laboratory_val, textvariable = laboratory)
        self.laboratorylist.set("Pick a laboratory")
        self.laboratorylist.pack()
        
        # add the add button 
        
        self.add_user_button = tk.Button(popup, text = 'Add user column', command = lambda : add_user_col(popup, firstname, lastname, status, laboratory, connection, grandparent))
        self.add_user_button.pack()
            
class StatusTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        
       #  define the first label holding the already defined users 
        self.label_status = tk.Label(self, text = 'Registered statuses', relief = 'ridge')
        self.label_status.pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM status')
            if res is not None:
                # define columns 
            
                col = ('id','name')
                
                # initiate treeview
                
                self.status_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
                # define headings
                
                self.status_tree.heading('id', text = 'id')
                self.status_tree.heading('name', text = 'Name')
                
                # get the values related to the user table
                
                val = None
                for status in res:
                    val = (status[0],
                           status[1])
                 
                    self.status_tree.insert('',tk.END, values = val)

                self.status_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(self, connection, 'status', parent)
                GUI_utils.AddButton(self, connection, 'status', parent)

                
            else:
                self.label_no_status = tk.Label(self, text = 'There is no data in the user table')
                self.label_no_status.pack()    

                
        else:
            self.label_no_status = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_status.pack()    
            
class StatusAdd():
    def __init__(self, popup, connection, grandparent):
        # add the first name values 
        self.name_lab = tk.Label(popup, text = 'Status Name')
        self.name_lab.pack()
        
        # define the firstname string value 
        
        name = tk.StringVar(popup)
        
        # get the entry for firstname 
       
        self.name_entry = tk.Entry(popup, textvariable = name)
        self.name_entry.pack()
        
        
        # add the add button 
        
        self.add_status_button = tk.Button(popup, text = 'Add status column', command = lambda : add_status_col(popup, name, connection, grandparent))
        self.add_status_button.pack()

class UniversityTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        
       #  define the first label holding the already defined users 
        self.label_status = tk.Label(self, text = 'Registered universities', relief = 'ridge')
        self.label_status.pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM university')
            if res is not None:
                # define columns 
            
                col = ('id','name','country','city','address')
                
                # initiate treeview
                
                self.university_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
                # define headings
                
                self.university_tree.heading('id', text = 'id')
                self.university_tree.heading('name', text = 'Name')
                self.university_tree.heading('country', text = 'Country')
                self.university_tree.heading('city', text = 'City')
                self.university_tree.heading('address', text = 'Address')

                # get the values related to the user table
                
                val = None
                for university in res:
                    val = (university[0],
                           university[1],
                           university[2],
                           university[3],
                           university[4])
                 
                    self.university_tree.insert('',tk.END, values = val)

                self.university_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(self, connection, 'university', parent)
                GUI_utils.AddButton(self, connection, 'university', parent)

                
            else:
                self.label_no_status = tk.Label(self, text = 'There is no data in the user table')
                self.label_no_status.pack()    

                
        else:
            self.label_no_status = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_status.pack()    

class UniversityAdd():
    def __init__(self, popup, connection, grandparent):
        # add the first name values 
        self.name_lab = tk.Label(popup, text = 'University Name')
        self.name_lab.pack()
        
        # define the firstname string value 
        
        name = tk.StringVar(popup)
        
        # get the entry for firstname 
       
        self.name_entry = tk.Entry(popup, textvariable = name)
        self.name_entry.pack()
        
        # add the country values 
        self.country_lab = tk.Label(popup, text = 'Country')
        self.country_lab.pack()
                
        country = tk.StringVar(popup)
       
        self.country_entry = tk.Entry(popup, textvariable = country)
        self.country_entry.pack()
    
        # add the city values 
        self.city_lab = tk.Label(popup, text = 'City')
        self.city_lab.pack()
                
        city = tk.StringVar(popup)
       
        self.city_entry = tk.Entry(popup, textvariable = city)
        self.city_entry.pack()
        
        # add the address values 
        self.address_lab = tk.Label(popup, text = 'Address')
        self.address_lab.pack()
                
        address = tk.StringVar(popup)
       
        self.address_entry = tk.Entry(popup, textvariable = address)
        self.address_entry.pack()
        
        # add the add button 
        
        self.add_university_button = tk.Button(popup, text = 'Add university column', command = lambda : add_university_col(popup, name, country, city, address, connection, grandparent))
        self.add_university_button.pack()

        
def add_user_col(popup, firstname, lastname, status, laboratory, connection, grandparent):
    
    # get the status id 
    status_id = database_utils.fetchall_query(connection, 'SELECT id FROM status WHERE name = "{}"'.format(status.get()))[0][0]
    
    # get the laboratory id 
    
    laboratory_id = database_utils.fetchall_query(connection, 'SELECT id FROM laboratory WHERE name = "{}"'.format(laboratory.get()))[0][0]
    
    table_update.add_row_user_table(firstname.get(), lastname.get(), status_id, laboratory_id, connection)
    
    # update the user table 
    popup.destroy()

    GUI_utils.update_table('user', connection, grandparent)

        
def add_status_col(popup, name, connection, grandparent):
    
    # get the status id 
    
    table_update.add_row_status_table(name.get(), connection)
    
    # update the user table 
    popup.destroy()

    GUI_utils.update_table('status', connection, grandparent)

def add_university_col(popup, name, country, city, address, connection, grandparent):
    
    # get the status id 
    
    table_update.add_row_university_table(name.get(), country.get(), city.get(), address.get(), connection)
    
    # update the user table 
    popup.destroy()

    GUI_utils.update_table('university', connection, grandparent)

def create_user_tabs(widget, connection):     
    # define the new tabs with user, status, laboratory and university 
    widget.tabcontrol_user = ttk.Notebook(widget)
    
    widget.tab_user = UserTree(widget.tabcontrol_user, connection)
    widget.tabcontrol_user.add(widget.tab_user, text = 'User')
    
    widget.tab_status = StatusTree(widget.tabcontrol_user, connection)
    widget.tabcontrol_user.add(widget.tab_status, text = 'Status')
    
    widget.tab_university = UniversityTree(widget.tabcontrol_user, connection)
    widget.tabcontrol_user.add(widget.tab_university, text = 'University')
    
    widget.tabcontrol_user.pack(expand = 1, fill = 'both')