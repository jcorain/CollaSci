'''
module where the different tables are created 
'''
import database_utils

def create_university_table(connection):
    """
    Function to create university table
    
    Parameters
    ----------
    connection : SQL connection.
        Connection to the SQL database

    Returns
    -------
    None.

    """
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
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
    
    database_utils.execute_query(connection, query)
    
def create_laboratory_table(connection):
    """
    Function to create the laboratory table
    
    Parameters
    ----------
    connection : SQL connection.
        Connection to the SQL database.

    Returns
    -------
    None.

    """
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    query = """
    CREATE TABLE IF NOT EXISTS laboratory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        university_id INT,
        FOREIGN KEY(university_id) REFERENCES university(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
    """
    
    # define the cursor and execute querry 
    
    database_utils.execute_query(connection, query)
    
def create_status_table(connection):
    """
    Function to create the status table
    
    Parameters
    ----------
    connection : SQL connection.
        Connection to the SQL database.

    Returns
    -------
    None.

    """
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    query = """
    CREATE TABLE IF NOT EXISTS status(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        );
    """
    
    # define the cursor and execute querry 
    
    database_utils.execute_query(connection, query)
    
    
def create_material_type_table(connection):
    """
    Function to create the material_type table
    
    Parameters
    ----------
    connection : SQL connection.
        Connection to the SQL database.

    Returns
    -------
    None.

    """
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    query = """
    CREATE TABLE IF NOT EXISTS material_type(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        );
    """
    
    # define the cursor and execute querry 
    
    database_utils.execute_query(connection, query)
    
def create_compound_table(connection):
     """
     Function to create the compound table
     
     Parameters
     ----------
     connection : SQL connection.
         Connection to the SQL database.

     Returns
     -------
     None.

     """
     
     # check connection 
     
     if connection is None:
         print('There is no connection to an SQL database. Please initiate it')
         return None
     
     query = """
     CREATE TABLE IF NOT EXISTS compound(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         formula VARCHAR(100),
         material_type_id INT,
         FOREIGN KEY(material_type_id) REFERENCES material_type(id) ON UPDATE CASCADE ON DELETE CASCADE
         );
     """
     
     # define the cursor and execute querry 
     
     database_utils.execute_query(connection, query)   

def create_experiment_type_table(connection):
    """
    Function to create the experiment_type table
    
    Parameters
    ----------
    connection : SQL connection.
        Connection to the SQL database.

    Returns
    -------
    None.

    """
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    query = """
    CREATE TABLE IF NOT EXISTS experiment_type(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        );
    """
    
    # define the cursor and execute querry 
    
    database_utils.execute_query(connection, query)