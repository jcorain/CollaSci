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
 
def update_user_table(firstname, lastname, status_id, laboratory_id, connection):
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
    if firstname is None:
        print('There is no user firstname. Please provide it')
        return None
    
    if lastname is None:
        print('There is no user lastname. Please provide it')
        return None
    
    
    if status_id is None:
        print('There is no status_id. Please provide it')
        return None

    if laboratory_id is None:
        print('There is no laboratory_id. Please provide it')
        return None

    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # set teh foreign keys on 
    
    connection.execute("PRAGMA foreign_keys = ON;")
    
    # check if the laboratory table exists 
    
    res = database_utils.check_table_exists(connection, 'user')
    
    if res == False:
        tables_create.create_user_table(connection)
        print('The user table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_firstname = database_utils.fetchall_query(connection, 'SELECT firstname FROM user')
        for val in existing_firstname:
            if val[0] == firstname:
                
                # check then the last name 
                existing_lastname = database_utils.fetchall_query(connection, "SELECT lastname FROM user WHERE firstname = '{}'".format(firstname))
                for val in existing_lastname:
                    if val[0] == lastname:

                        # check then the laboratory 
                        existing_laboratory_id = database_utils.fetchall_query(connection, "SELECT laboratory_id FROM user WHERE firstname = '{}' AND lastname = '{}'".format(firstname, lastname))
                        for val in existing_laboratory_id:
                            if val[0] == laboratory_id:
                                # get the laboratory_id name 
                                laboratory_name = database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(laboratory_id))[0][0]
                                print('The user {} {} ({}) already exists and will not be added to the database.'.format(firstname, lastname, laboratory_name))
                                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        user(firstname, lastname, status_id, laboratory_id)
    VALUES
        (?, ?, ?, ?)
    """
    
    res_exec = database_utils.execute_query(connection, query, values = (firstname, lastname, status_id, laboratory_id))
    
    if res_exec:
        laboratory_name = database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(laboratory_id))[0][0]
        print('The user {} {} ({}) has been succesfully added to the database.'.format(firstname, lastname, laboratory_name))


def update_experiment_setup_table(name, room_name, start_date, min_field, max_field, min_temperature, max_temperature,
                                   experiment_type_id, responsible_id, connection):
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
        print('There is no experiment setup name. Please provide it')
        return None
    
    if room_name is None:
        print('There is no experiment setup room name. Please provide it')
        return None
    
    
    if start_date is None:
        print('There is no experiment setup start date. Please provide it')
        return None

    if experiment_type_id is None:
        print('There is no experiment_type_id for the experiment setup. Please provide it')
        return None

    if responsible_id is None:
        print('There is no responsible_id for the experiment setup. Please provide it')
        return None
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # set teh foreign keys on 
    
    connection.execute("PRAGMA foreign_keys = ON;")
    
    # check if the laboratory table exists 
    
    res = database_utils.check_table_exists(connection, 'experiment_setup')
    
    if res == False:
        tables_create.create_experiment_setup_table(connection)
        print('The experiment table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_name = database_utils.fetchall_query(connection, 'SELECT name FROM experiment_setup;')
        for val in existing_name:
            if val[0] == name:
                print('The experiment setup {} already exists and will not be added to the database.'.format(name))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        experiment_setup(name, room_name, start_date, min_field, max_field, min_temperature, max_temperature,
                         experiment_type_id, responsible_id)
    VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    res_exec = database_utils.execute_query(connection, query, 
                                            values = (name, room_name, start_date, min_field, 
                                                      max_field, min_temperature, max_temperature,
                                                      experiment_type_id, responsible_id))
    
    if res_exec:
        print('The experiment setup {} has been succesfully added to the database.'.format(name))

        
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
    
    print('\ncreate the first user\n')
    
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 1
    laboratory_id = 1
    update_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\ncreate the second user\n')
    
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 2
    laboratory_id = 3
    update_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\ncreate the third user\n')
    
    user_firstname = 'Gediminas'
    user_lastname = 'Simutis'
    status_id = 2
    laboratory_id = 3
    update_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    update_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\nTest user without status id.\n')
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 3
    laboratory_id = 2
    update_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\nTest user without laboratory id.\n')
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 2
    laboratory_id = 4
    update_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\ncheck user table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM user;").fetchall())
    cur.close()

    print('\ncreate the first experimental setup\n')
    
    experimental_setup_name = 'MMPS He4'
    roomname = 'Salon'
    experimental_setup_start_date = '25/05/2018'
    min_field = 0
    max_field = 5
    min_temperature = 1.5
    max_temperature = 300
    experiment_type_id = 1
    responsible_id = 1
    update_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                    max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    print('\ncreate the second experimental setup\n')
    
    experimental_setup_name = 'MMPS He4 bis'
    roomname = 'Salon'
    experimental_setup_start_date = '25/05/2018'
    min_field = None
    max_field = None
    min_temperature = None
    max_temperature = None
    experiment_type_id = 1
    responsible_id = 2
    update_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                    max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    update_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    print("\nTest wrong experiment type for experiment setup\n")
    
    experimental_setup_name = 'MMPS with wrong experiement type'
    roomname = 'Salon'
    experimental_setup_start_date = '25/05/2018'
    min_field = None
    max_field = None
    min_temperature = None
    max_temperature = None
    experiment_type_id = 5
    responsible_id = 2
    update_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                    max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    print("\nTest wrong responsible type for experiment setup\n")
    
    experimental_setup_name = 'MMPS with wrong responsible'
    roomname = 'Salon'
    experimental_setup_start_date = '25/05/2018'
    min_field = None
    max_field = None
    min_temperature = None
    max_temperature = None
    experiment_type_id = 1
    responsible_id = 6
    update_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                    max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    print('\ncheck experiment setup table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM experiment_setup;").fetchall())
    cur.close()
    
    print('\ncheck all the tables values\n')
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM university;").fetchall())
    print(cur.execute("SELECT * FROM laboratory;").fetchall())
    print(cur.execute("SELECT * FROM status;").fetchall())
    print(cur.execute("SELECT * FROM material_type;").fetchall())
    print(cur.execute("SELECT * FROM compound;").fetchall())
    print(cur.execute("SELECT * FROM experiment_type;").fetchall())
    print(cur.execute("SELECT * FROM user;").fetchall())
    print(cur.execute("SELECT * FROM experiment_setup;").fetchall())

    cur.close()
    
    # close the connection
    connection.close()