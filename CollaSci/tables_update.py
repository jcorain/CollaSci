"""
module to update tables 
"""

import database_utils
import tables_create

# set the foreign_keys on 

def update_university_table(name, country, city, address, connection):
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
    connection : SQL connection.
        Connection to the SQL database

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
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    # check if the university table exists 
    
    res = database_utils.check_table_exists(connection, 'university')
        
    if res == False:
        tables_create.create_university_table(connection)
        print('The university table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT name FROM university')

        for val in existing_values:
            if val[0] == name:
                print('The university {} already exists and will not be added to the database.'.format(name))
                return None
    # create the cursor 
        
    query = """
    INSERT INTO 
        university(name, country, city, address)
    VALUES
        (?, ?, ?, ?)
    """
    
    res_exec = database_utils.execute_query(connection, query, values = (name, country, city, address))
    
    if res_exec:    
        print('The university {} has been succesfully added to the database.'.format(name))
    
        
    
def update_laboratory_table(name, university_id, connection):
    '''
    function to update laboratory table data

    Parameters
    ----------
    name : str
        Name of the laboratory.
    university_id : int
        ID of the university related to the laboratory

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if name is None:
        print('There is no laboratory name. Please provide it')
        return None
    
    if university_id is None:
        print('There is no university_id. Please provide it')
        return None
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # set teh foreign keys on 
    
    connection.execute("PRAGMA foreign_keys = ON;")
    
    # check if the laboratory table exists 
    
    res = database_utils.check_table_exists(connection, 'laboratory')
    
    if res == False:
        tables_create.create_laboratory_table(connection)
        print('The laboratory table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT name FROM laboratory')
        for val in existing_values:
            if val[0] == name:
                print('The laboratory {} already exists and will not be added to the database.'.format(name))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        laboratory(name, university_id)
    VALUES
        (?, ?)
    """
    
    res_exec = database_utils.execute_query(connection, query, values = (name, university_id))
    
    if res_exec:
        print('The laboratory {} has been succesfully added to the database.'.format(name))
        
        
def update_status_table(name, connection):
    '''
    function to update status table data

    Parameters
    ----------
    name : str
        Name of the status.

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if name is None:
        print('There is no status name. Please provide it')
        return None
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # check if the status table exists 
    
    res = database_utils.check_table_exists(connection, 'status')
    
    if res == False:
        tables_create.create_status_table(connection)
        print('The staus table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT name FROM status')
        for val in existing_values:
            if val[0] == name:
                print('The status {} already exists and will not be added to the database.'.format(name))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        status(name)
    VALUES
        (?)
    """
    
    res_exec = database_utils.execute_query(connection, query, values = (name,))
    
    if res_exec:
        print('The status {} has been succesfully added to the database.'.format(name))
        
def update_material_type_table(name, connection):
    '''
    function to update the material type table data

    Parameters
    ----------
    name : str
        Name of the material type.

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if name is None:
        print('There is no material type name. Please provide it')
        return None
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # check if the status table exists 
    
    res = database_utils.check_table_exists(connection, 'material_type')
    
    if res == False:
        tables_create.create_material_type_table(connection)
        print('The material_type table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT name FROM material_type')
        for val in existing_values:
            if val[0] == name:
                print('The material_type {} already exists and will not be added to the database.'.format(name))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        material_type(name)
    VALUES
        (?)
    """
    
    res_exec = database_utils.execute_query(connection, query, values = (name,))
    
    if res_exec:
        print('The material_type {} has been succesfully added to the database.'.format(name))
        
def update_compound_table(name, formula, material_type_id, connection):
    '''
    function to update compound table data

    Parameters
    ----------
    name : str
        Name of the compound.
    formula : str
        Chemical formula of the compound.
    material_type_id : int
        ID of the material_type related to the laboratory

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if name is None:
        print('There is no compound name. Please provide it')
        return None
    
    if formula is None:
        print('There is no compound formula. Please provide it')
        return None
    
    
    if material_type_id is None:
        print('There is no material_type_id. Please provide it')
        return None
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # set teh foreign keys on 
    
    connection.execute("PRAGMA foreign_keys = ON;")
    
    # check if the laboratory table exists 
    
    res = database_utils.check_table_exists(connection, 'compound')
    
    if res == False:
        tables_create.create_compound_table(connection)
        print('The compound table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT name FROM compound')
        for val in existing_values:
            if val[0] == name:
                print('The compound {} already exists and will not be added to the database.'.format(name))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        compound(name, formula, material_type_id)
    VALUES
        (?, ?, ?)
    """
    
    res_exec = database_utils.execute_query(connection, query, values = (name, formula, material_type_id))
    
    if res_exec:
        print('The compound {} has been succesfully added to the database.'.format(name))
        
def update_experiment_type_table(name, connection):
    '''
    function to update the experiment type table data

    Parameters
    ----------
    name : str
        Name of the experiment type.

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if name is None:
        print('There is no experiment type name. Please provide it')
        return None
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # check if the status table exists 
    
    res = database_utils.check_table_exists(connection, 'experiment_type')
    
    if res == False:
        tables_create.create_experiment_type_table(connection)
        print('The experiment_type table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT name FROM experiment_type')
        for val in existing_values:
            if val[0] == name:
                print('The experiment_type {} already exists and will not be added to the database.'.format(name))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        experiment_type(name)
    VALUES
        (?)
    """
    
    res_exec = database_utils.execute_query(connection, query, values = (name,))
    
    if res_exec:
        print('The experiment_type {} has been succesfully added to the database.'.format(name))
        
        
if __name__ == '__main__':
    
    print('\nCreate connection to the database\n')
    
    connection = database_utils.create_or_connect_db()
    
    print('create the first university\n')
    
    university_name = 'Université Paris Saclay'
    university_country = 'France'
    university_city = 'Gif-sur-Yvette'
    university_address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
    update_university_table(university_name, university_country, university_city, university_address, connection)
    
    print('\ncheck what happens if we recreate the entry\n') 
    
    update_university_table(university_name, university_country, university_city, university_address, connection)
    
    print('\ncreate the second university\n')
    
    university_name = 'Paul Scherrer Institute'
    university_country = "Switzerland"
    university_city = 'Villigen'
    university_address = 'PSI CH, Forschungsstrasse 111, 5232 Villigen'
    update_university_table(university_name, university_country, university_city, university_address, connection)
    
    
    print('\ncheck university table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM university;").fetchall())
    cur.close()
    
    print('\ncreate the first laboratory\n') 
    
    laboratory_name = 'Laboratoire de Physique des Solides'
    university_id = 1
    update_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n') 
    
    update_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncreate the second laboratory\n')
    
    laboratory_name = 'Laboratoire de Physique Théoriques et de Modèles Statistiques'
    university_id = 1
    update_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncreate the third laboratory\n') 
    
    laboratory_name = 'Laboratory for Muon Spin Spectroscopy'
    university_id = 2
    update_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncheck what happens when the university does not exist\n') 

    laboratory_name = 'Laboratoire test'
    university_id = 3
    update_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncheck laboratory table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM laboratory;").fetchall())
    cur.close()
    
    print('\ncreate the first status\n')
    
    status_name = 'PhD Student'
    update_status_table(status_name, connection)
    
    print('\ncreate the second status\n')
    
    status_name = 'Postdoc'
    update_status_table(status_name, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    update_status_table(status_name, connection)
    
    print('\ncheck status table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM status;").fetchall())
    cur.close()
    
    print('\ncreate the first material type\n')
    
    material_type_name = 'Quantum Spin Liquid'
    update_material_type_table(material_type_name, connection)
    
    print('\ncreate the second material type\n')
    
    material_type_name = 'Superconductor'
    update_material_type_table(material_type_name, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    update_material_type_table(material_type_name, connection)
    
    print('\ncheck material_type table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM material_type;").fetchall())
    cur.close()
    
    print('\ncreate the first compound\n')
    
    compound_name = 'DQVOF'
    compound_formula = '(NH4)2[C7H14N][V7O6F18]'
    material_type_id = 1
    update_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    print('\ncreate the second compound\n')
    
    compound_name = 'Herbertsmithite'
    compound_formula = 'ZnCu3(OH)6Cl2'
    material_type_id = 1
    update_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    update_compound_table(compound_name, compound_formula, material_type_id, connection)
     
    print('\ncreate the third compound\n')
    
    compound_name = 'YBACUO'
    compound_formula = 'YBa2Cu3O7'
    material_type_id = 2
    update_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    print('Test compound without material type')
    compound_name = 'test'
    compound_formula = 'test'
    material_type_id = 3
    update_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    print('\ncheck compound table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM compound;").fetchall())
    cur.close()
    
    print('\ncreate the first experiement type\n')
    
    experiment_type_name = 'Heat Capacity vs Temperature'
    update_experiment_type_table(experiment_type_name, connection)
    
    print('\ncreate the second experiement type\n')
    
    experiment_type_name = 'Magnetization vs Temperature'
    update_experiment_type_table(experiment_type_name, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    update_experiment_type_table(experiment_type_name, connection)
    
    print('\ncheck experiment_type table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM experiment_type;").fetchall())
    cur.close()
    
    print('\ncheck all the tables values\n')
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM university;").fetchall())
    print(cur.execute("SELECT * FROM laboratory;").fetchall())
    print(cur.execute("SELECT * FROM status;").fetchall())
    print(cur.execute("SELECT * FROM material_type;").fetchall())
    print(cur.execute("SELECT * FROM compound;").fetchall())
    print(cur.execute("SELECT * FROM experiment_type;").fetchall())
    cur.close()
    
    # close the connection
    connection.close()