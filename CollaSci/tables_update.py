"""
module to update tables 
"""

import database_connect
import tables_create
import os
import sqlite3

def check_table_exists(table_name, path = os.path.dirname(os.getcwd()), dbname = 'database.sqlite'):
    '''
    function to check if a table exists

    Parameters
    ----------
    table_name : str
        name of the table.

    Returns
    -------
    None.

    '''
    if table_name is None:
        print('There is no table name. Please provide it.')
        return None
    
    # connect to the database
    connection = database_connect.create_or_connect_db(path = path, name = dbname)
    
    # check if the university table exists 
       
    cur = connection.cursor()
    
    check_table = cur.execute("SELECT COUNT(name) FROM sqlite_master WHERE type = 'table';")
    res = check_table.fetchall()
    
    check_table.close()
    connection.close()
    
    if (table_name,) in res:
        return True
    else:
        return False

def update_university_table(name, country, city, address, path = os.path.dirname(os.getcwd()), dbname = 'database.sqlite'):
    '''
    function to update university table data

    Parameters
    ----------
    name : str
        Name of the university or institution.
    country : str
        Country of the university.
    city : str
        City of the university.
    address : str
        Address of the university.

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if name is None:
        print('There is no university name. Please provide it')
        return None
    
    if country is None:
        print('There is no university country. Please provide it')
        return None
    
    if city is None:
        print('There is no university city. Please provide it')
        return None
    
    if address is None:
        print('There is no university address. Please provide it')
        return None
    
    # create connection 
    
    # connect to the database
    connection = database_connect.create_or_connect_db(path = path, name = dbname)
    
    # check if the university table exists 
    
    res = check_table_exists('university', path, dbname)
    
    if res == False:
        tables_create.create_university_table(path, dbname)
        print('The university table has been created.')
    
    # create the cursor 
        
    query = """
    INSERT INTO 
        university(name, country, city, address)
    VALUES
        (?, ?, ?, ?)
    """
    
    tables_create.execute_query(connection, query, task = (name, country, city, address))
    
    connection.close()
    
if __name__ == '__main__':
    name = 'Université Paris Saclay'
    country = 'France'
    city = 'Gif-sur-Yvette'
    address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
    update_university_table(name, country, city, address)