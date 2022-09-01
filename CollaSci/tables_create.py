'''
module where the different tables are created 
'''
import database_utils

def create_university_table(connection):
    """
    function to create university table
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
        FOREIGN KEY(university_id) REFERENCES university(id)
        );
    """
    
    # define the cursor and execute querry 
    
    database_utils.execute_query(connection, query)
        
    
if __name__ == '__main__':
    create_laboratory_table()
