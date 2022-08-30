"""
module used to create and be connected to the database
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
    None.

    '''
    # create a connection 
    database_path = os.path.join(path, name)
   
    connection = None
    
    try:
        connection = sqlite3.connect(database_path)
        print('Connection to SQLite DB {} succesfull'.format(database_path))
    except sqlite3.Error as e:
        print('The error {} occured'.format(e))
        
    return connection 
        
    
   
if __name__ == '__main__':
    connection = create_or_connect_db()