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
        tk.Label(self, text = 'Registered users', relief = 'ridge').pack()  
        
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
                tk.Label(self, text = 'There is no data in the user table').pack()    
             
        else:
            tk.Label(self, text = 'There is no SQL connection').pack()    
  
class UserAdd():
    def __init__(self, popup, connection, grandparent):
        # add the first name values 
        firstname_entry = GUI_utils.AddValueEntry(popup, connection, grandparent, 'First Name')
        firstname = firstname_entry.value
        
        # add the last name values 
        lastname_entry = GUI_utils.AddValueEntry(popup, connection, grandparent, 'Last Name')
        lastname = lastname_entry.value
        
        # add the status values 
        
        status_entry = GUI_utils.AddValueList(popup, connection, grandparent, 'Status', 'status')
        status = status_entry.value
        
        # add the laboratory values 
        
        laboratory_entry = GUI_utils.AddValueList(popup, connection, grandparent, 'Laboratory', 'laboratory')
        laboratory = laboratory_entry.value
        
        # add the add button 
        
        tk.Button(popup, text = 'Add user column', 
                  command = lambda : add_user_col(popup, 
                                                  firstname, 
                                                  lastname, 
                                                  status, 
                                                  laboratory, 
                                                  connection, 
                                                  grandparent)).pack()
            
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
                self.label_no_status = tk.Label(self, text = 'There is no data in the status table')
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
                self.label_no_laboratory = tk.Label(self, text = 'There is no data in the university table')
                self.label_no_laboratory.pack()    

                
        else:
            self.label_no_laboratory = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_laboratory.pack()    

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

class LaboratoryTree(tk.Frame):
    def __init__(self, parent, connection): 
        tk.Frame.__init__(self, parent)
        # get a table with the connection 
        
       #  define the first label holding the already defined users 
        self.label_laboratory = tk.Label(self, text = 'Registered laboratories', relief = 'ridge')
        self.label_laboratory.pack()  
        
        if connection is not None:
            # get the results from the user database
            res = database_utils.fetchall_query(connection, 'SELECT * FROM laboratory')
            if res is not None:
                # define columns 
            
                col = ('id','name','university')    
                
                # initiate treeview
                
                self.laboratory_tree = ttk.Treeview(self, columns = col, show = 'headings')
                
                # define headings
                
                self.laboratory_tree.heading('id', text = 'id')
                self.laboratory_tree.heading('name', text = 'Name')
                self.laboratory_tree.heading('university', text = 'University')
            
                # get the values related to the user table
                
                val = None
                for laboratory in res:
                    val = (laboratory[0],
                           laboratory[1],
                           database_utils.fetchall_query(connection, 'SELECT name FROM university WHERE id = {}'.format(laboratory[2]))[0][0])
                 
                    self.laboratory_tree.insert('',tk.END, values = val)

                self.laboratory_tree.pack(expand = True, fill = 'both')
                
                # add the delete frame 
                
                GUI_utils.DeleteButton(self, connection, 'laboratory', parent)
                GUI_utils.AddButton(self, connection, 'laboratory', parent)

                
            else:
                self.label_no_laboratory = tk.Label(self, text = 'There is no data in the laboratory table')
                self.label_no_laboratory.pack()    

                
        else:
            self.label_no_laboratory = tk.Label(self, text = 'There is no SQL connection')
            self.label_no_laboratory.pack()    

       
       
class LaboratoryAdd():
    def __init__(self, popup, connection, grandparent):
        # add the name values 
        self.name_lab = tk.Label(popup, text = 'Name')
        self.name_lab.pack()
                
        name = tk.StringVar(popup)
        
        self.name_entry = tk.Entry(popup, textvariable = name)
        self.name_entry.pack()

        # add the universities values 
        
        self.university_lab = tk.Label(popup, text = 'University (if the university you want does not exist in the list please update the university table.')
        self.university_lab.pack()
        
        #define the status string value 
       
        university = tk.StringVar(popup)
        
        # get the list of existing status 
        university_val = [val[0] for val in database_utils.fetchall_query(connection, 'SELECT name FROM university')]
 
        self.universitylist = ttk.Combobox(popup, values = university_val, textvariable = university)
        self.universitylist.set("Pick a university")
        self.universitylist.pack()
        
        # add the add button 
        
        self.add_laboratory_button = tk.Button(popup, text = 'Add user column', command = lambda : add_laboratory_col(popup, name, university, connection, grandparent))
        self.add_laboratory_button.pack()


        
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


def add_laboratory_col(popup, name, university, connection, grandparent):
    
    # get the university id 
    university_id = database_utils.fetchall_query(connection, 'SELECT id FROM university WHERE name = "{}"'.format(university.get()))[0][0]

    
    # get the status id 
    
    table_update.add_row_laboratory_table(name.get(), university_id, connection)

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
    
    widget.tab_laboratory = LaboratoryTree(widget.tabcontrol_user, connection)
    widget.tabcontrol_user.add(widget.tab_laboratory, text = 'Laboratory')
    
    widget.tabcontrol_user.pack(expand = 1, fill = 'both')