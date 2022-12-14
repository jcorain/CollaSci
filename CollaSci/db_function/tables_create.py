'''
module where the different tables are created 
'''
import CollaSci.db_function.database_utils as database_utils

# from . import database_utils as 

# import database_utils

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
    
    database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
    query = """
    CREATE TABLE IF NOT EXISTS laboratory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        university_id INT NOT NULL,
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
     
     database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
     query = """
     CREATE TABLE IF NOT EXISTS compound(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         formula VARCHAR(100) NOT NULL,
         material_type_id INT NOT NULL,
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
    
def create_user_table(connection):
     """
     Function to create the user table
     
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
     
     database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
     query = """
     CREATE TABLE IF NOT EXISTS user(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         firstname VARCHAR(100) NOT NULL,
         lastname VARCHAR(100) NOT NULL,
         status_id INT NOT NULL,
         laboratory_id INT NOT NULL,
         FOREIGN KEY(status_id) REFERENCES status(id) ON UPDATE CASCADE ON DELETE CASCADE,
         FOREIGN KEY(laboratory_id) REFERENCES laboratory(id) ON UPDATE CASCADE ON DELETE CASCADE
         );
     """
     
     # define the cursor and execute querry 
     
     database_utils.execute_query(connection, query)
     
def create_experiment_setup_table(connection):
     """
     Function to create the experiment_setup table
     
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
     
     database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
     query = """
     CREATE TABLE IF NOT EXISTS experiment_setup(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         room_name TEXT NOT NULL,
         start_date DATE NOT NULL,
         min_field REAL,
         max_field REAL,
         min_temperature REAL,
         max_temperature REAL,
         experiment_type_id INT NOT NULL,
         responsible_id INT NOT NULL,
         FOREIGN KEY(experiment_type_id) REFERENCES experiment_type(id) ON UPDATE CASCADE ON DELETE CASCADE,
         FOREIGN KEY(responsible_id) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE
         );
     """
     
     # define the cursor and execute querry 
     
     database_utils.execute_query(connection, query)
     
def create_batch_table(connection):
     """
     Function to create the batch table
     
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
     
     database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
     query = """
     CREATE TABLE IF NOT EXISTS batch(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         mass REAL NOT NULL,
         color VARCHAR(50) NOT NULL,
         type VARCHAR(50) NOT NULL,
         creation_date DATE NOT NULL, 
         compound_id INT NOT NULL,
         grower_id INT NOT NULL,
         FOREIGN KEY(compound_id) REFERENCES compound(id) ON UPDATE CASCADE ON DELETE CASCADE,
         FOREIGN KEY(grower_id) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE
         );
     """
     
     # define the cursor and execute querry 
     
     database_utils.execute_query(connection, query)
     
def create_project_table(connection):
     """
     Function to create the project table
     
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
     
     database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
     query = """
     CREATE TABLE IF NOT EXISTS project(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         responsible_id INT NOT NULL,
         FOREIGN KEY(responsible_id) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE
         );
     """
     
     # define the cursor and execute querry 
     
     database_utils.execute_query(connection, query)
     
def create_data_table(connection):
     """
     Function to create the data table
     
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
     
        
     database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")  
     query = """
     CREATE TABLE IF NOT EXISTS data(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         mass REAL NOT NULL,
         experiment_no INT NOT NULL,
         field REAL, 
         temp REAL,
         date DATE NOT NULL,
         path_import TEXT NOT NULL,
         new_path TEXT NOT NULL,
         comment TEXT, 
         experiment_setup_id INT NOT NULL,
         user_id INT NOT NULL,
         batch_id INT NOT NULL,
         project_id INT NOT NULL,
         FOREIGN KEY(experiment_setup_id) REFERENCES experiment_setup(id) ON UPDATE CASCADE ON DELETE CASCADE,
         FOREIGN KEY(user_id) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE,
         FOREIGN KEY(batch_id) REFERENCES batch(id) ON UPDATE CASCADE ON DELETE CASCADE,
         FOREIGN KEY(project_id) REFERENCES project(id) ON UPDATE CASCADE ON DELETE CASCADE
         );
     """
     
     # define the cursor and execute querry 
     
     database_utils.execute_query(connection, query)  