'''
module where the different tables are created 
'''
import database_connect
import os
import sqlite3


def execute_query(connection, query, task = None):
    
    
    cursor = connection.cursor()
    try:
        if task is None:
            cursor.execute(query)
        else:
            cursor.execute(query, task)
        connection.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    
    #close the cursor
    cursor.close()


def create_university_table(path = os.path.dirname(os.getcwd()), dbname = 'database.sqlite'):
    """
    Parameters
    ----------
    path : str, optional
        path to the database. The default is os.path.dirname(os.getcwd()).
    dbname : TYPE, optional
        database name. The default is 'database.sqlite'.

    Returns
    -------
    None.

    """
    # connect to the database
    connection = database_connect.create_or_connect_db(path = path, name = dbname)
    
    # create the query 
    
    query = """
    CREATE TABLE IF NOT EXISTS university(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        country VARCHAR(100) NOT NULL, 
        city VARCHAR(100) NOT NULL,
        address TEXT NOT NULL
        );
    """
    
    # define the cursor and execute querry 
    
    execute_query(connection, query)
        
    # close the connection
    
    connection.close()
    
if __name__ == '__main__':
    create_university_table()

# def create_data_table(path = os.path.dirname(os.getcwd()), dbname = 'database.sqlite'):
#     """
    

#     Parameters
#     ----------
#     path : str, optional
#         path to the database. The default is os.path.dirname(os.getcwd()).
#     dbname : TYPE, optional
#         database name. The default is 'database.sqlite'.

#     Returns
#     -------
#     None.

#     """
#     # connect to the database
#     connection = database_connect.create_or_connect_db(path = path, name = dbname)
    
#     # create the query 
    
#     querry = """
#     CREATE TABLE IF NOT EXISTS data(
#         id INTEGER PRMARY KEY AUTOINCREMENT,
#         date DATE NOT  NULL,
#         magnetic_field NUMERIC, 
#         temperature NUMERIC,
        
#         );
#     """
    
