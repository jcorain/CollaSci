"""
module used for utils function related to the database
"""

import sqlite3
import os

def create_or_connect_db(path = os.path.dirname(os.getcwd()), name = 'database.sqlite'):
    '''
    Function to create a new database

    Parameters
    ----------
    path : str
        path to the database.
    name : str
        database name.

    Returns
    -------
    connection : SQL connection
        The connection to the database.

    '''
    # create a connection 
    database_path = os.path.join(path, name)
   
    connection = None
    
    try:
        connection = sqlite3.connect(database_path)
        print('Connection to SQLite DB {} succesfull'.format(database_path))
    except sqlite3.Error as e:
        print('The error {} occured'.format(e))
        connection = None
        
    return connection 
        

def execute_query(connection, query, values = None):
    '''
    Function to commit some querry to the database with or without values 

    Parameters
    ----------
    connection : SQL connection
        Connection to the SQL database.
    query : str
        Query to commit.
    values : tupple, optional
        Tupple containing the values to be iserted into tables if needed. The default is None.

    Returns
    -------
    Boolean : 
        True if the execution has been made without errors.

    '''
    cursor = connection.cursor()
    try:
        if values is None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)
        connection.commit()
        print("Query executed successfully")
        #close the cursor
        cursor.close()
        return True
    
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        #close the cursor
        cursor.close()
        return False
    
    

def fetchall_query(connection, query):
    '''
    Function to fetch all the values from a querry 
    
    Parameters
    ----------
    connection : SQL Connection
        Connection to the SQL database    
    query : str
        Query for the database to fetch.

    Returns
    -------
    res : list
        List containing the different tupples.

    '''
    cursor = connection.cursor()
    try:
        res = cursor.execute(query).fetchall()
        print("Query fetched successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        res = None

    #close the cursor
    cursor.close()
    return res

def check_table_exists(connection, table_name):
    '''
    function to check if a table exists

    Parameters
    ----------
    connection : SQL connection.
        The connection to the SQL database.
    table_name : str
        name of the table.

    Returns
    -------
    Boolean 
        True if the table exists.

    '''
    if table_name is None:
        print('There is no table name. Please provide it.')
        return None
    
    # check if the university table exists 
       
    cur = connection.cursor()
    
    check_table = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    res = check_table.fetchall()
        
    check_table.close()
    
    if (table_name,) in res:
        return True
    else:
        return False
   
if __name__ == '__main__':
    connection = create_or_connect_db()