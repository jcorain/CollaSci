"""
module to change tables 
"""

# import CollaSci

import CollaSci.db_function.database_utils as database_utils
import CollaSci.db_function.tables_create as tables_create

# import database_utils
# import tables_create

import os
import shutil

# set the foreign_keys on 

def add_row_university_table(name, country, city, address, connection):
    '''
    function to add row to  university table data

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
    
        
    
def add_row_laboratory_table(name, university_id, connection):
    '''
    function to add row to  laboratory table data

    Parameters
    ----------
    name : str
        Name of the laboratory.
    university_id : int
        ID of the university related to the laboratory
    connection : SQL connection.
        Connection to the SQL database

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
    
    # set the foreign keys on 
    
    database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
    
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
        
        
def add_row_status_table(name, connection):
    '''
    function to add row to  status table data

    Parameters
    ----------
    name : str
        Name of the status.
    connection : SQL connection.
        Connection to the SQL database

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
        
def add_row_material_type_table(name, connection):
    '''
    function to add row to  the material type table data

    Parameters
    ----------
    name : str
        Name of the material type.
    connection : SQL connection.
        Connection to the SQL database

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
        
def add_row_compound_table(name, formula, material_type_id, connection):
    '''
    function to add row to  compound table data

    Parameters
    ----------
    name : str
        Name of the compound.
    formula : str
        Chemical formula of the compound.
    material_type_id : int
        ID of the material_type related to the compound
    connection : SQL connection.
        Connection to the SQL database

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
    
    database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
    
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
        
def add_row_experiment_type_table(name, connection):
    '''
    function to add row to  the experiment type table data

    Parameters
    ----------
    name : str
        Name of the experiment type.
    connection : SQL connection.
        Connection to the SQL database

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
 
def add_row_user_table(firstname, lastname, status_id, laboratory_id, connection):
    '''
    function to add row to  compound table data

    Parameters
    ----------
    firstname : str
        Firtsname of the user.
    Lastname : str
        Lastname of the user.
    status_id : int
        ID of the status related to the user
    laboratory_id : int
        ID of the user laboratory
    connection : SQL connection.
        Connection to the SQL database

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
    
    database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
    
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


def add_row_experiment_setup_table(name, room_name, start_date, min_field, max_field, min_temperature, max_temperature,
                                   experiment_type_id, responsible_id, connection):
    '''
    function to add row to  experiment setup table data

    Parameters
    ----------
    name : str
        Name of the experiment setup.
    room_name : str
        name of the room where the setup is situated.
    start_date : date
        date when the experiment has been setup
    min_field : float
        minimum magnetic field in T (can be None)
    max_field : float
        maximum magnetic field in T (can be None)
    min_temperature : float
        minimum temperature in K (can be None)
    max_temperature : float
        maximum temperature in K (can be None)
    experiment_type_id : int
        id related to the experiment type
    responsible_id : int
        id related to the user responsble for the experiment setup
    connection : SQL connection.
        Connection to the SQL database

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
    
    database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
    
    # check if the laboratory table exists 
    
    res = database_utils.check_table_exists(connection, 'experiment_setup')
    
    if res == False:
        tables_create.create_experiment_setup_table(connection)
        print('The experiment setup table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_name = database_utils.fetchall_query(connection, 'SELECT name FROM experiment_setup;')
        for val in existing_name:
            if val[0] == name:
                # get the existing responsible id 
                existing_responsible_id = database_utils.fetchall_query(connection, 'SELECT responsible_id FROM experiment_setup WHERE name = "{}";'.format(name))
                for val_id in existing_responsible_id:
                    if val_id[0] == responsible_id:
                        responsible_name = database_utils.fetchall_query(connection, 'SELECT firstname, lastname FROM user WHERE id = {};'.format(responsible_id))[0]
                        print('The experiment setup {} under the responsibility of {} {} already exists and will not be added to the database.'.format(name, responsible_name[0], responsible_name[1]))
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


def add_row_batch_table(name, mass, color, Type, creation_date, compound_id, grower_id, connection):
    '''
    function to add row to  batch table data

    Parameters
    ----------
    name : str
        Name of the batch
    mass : float
        Mass synthetized in g
    color : str
        Principal color of the batch
    Type : str 
        Type of the batch (powder, single cristal, polycristal)
    creation_date : date
        Creation date of the batch
    compound_id : int
        id related to the batch compound
    grower_id : int
        ID of the user who grows the batch
    connection : SQL connection.
        Connection to the SQL database

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if name is None:
        print('There is no batch name. Please provide it')
        return None
    
    if mass is None:
        print('There is no batch mass. Please provide it')
        return None
    
    
    if color is None:
        print('There is no batch color. Please provide it')
        return None

    if Type not in ['powder','polycristal','single cristal']:
        print('The batch type is not in the list "powder", "polycristal" or "single cristal". Please make a choice')
        return None

    if creation_date is None:
        print('There is no batch creation date. Please provide it')
        return None
    
    if compound_id is None:
        print('There is no compound_id for the batch. Please provide it')
        return None
    
    if grower_id is None:
        print('There is no grower_id for the batch. Please provide it')
        return None
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # set teh foreign keys on 
    
    database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
    
    # check if the laboratory table exists 
    
    res = database_utils.check_table_exists(connection, 'batch')
    
    if res == False:
        tables_create.create_batch_table(connection)
        print('The batch table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_name = database_utils.fetchall_query(connection, 'SELECT name FROM batch;')
        for val in existing_name:
            if val[0] == name:
                print('The batch {} already exists and will not be added to the database.'.format(name))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        batch(name, mass, color, type, creation_date, compound_id, grower_id)
    VALUES
        (?, ?, ?, ?, ?, ?, ?)
    """
    
    res_exec = database_utils.execute_query(connection, query, 
                                            values = (name, mass, color, Type, creation_date,
                                                      compound_id, grower_id))
    
    if res_exec:
        print('The batch {} has been succesfully added to the database.'.format(name))


def add_row_project_table(name, responsible_id, connection):
    '''
    function to add row to project table data

    Parameters
    ----------
    name : str
        Name of the experiment setup.
    responsible_id : int
        id related to the user responsble for the project
    connection : SQL connection.
        Connection to the SQL database

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if name is None:
        print('There is no project name. Please provide it')
        return None

    if responsible_id is None:
        print('There is no responsible_id for the experiment setup. Please provide it')
        return None
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # set teh foreign keys on 
    
    database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
    
    # check if the laboratory table exists 
    
    res = database_utils.check_table_exists(connection, 'project')
    
    if res == False:
        tables_create.create_project_table(connection)
        print('The project table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:
        # get the existing values 
        
        existing_name = database_utils.fetchall_query(connection, 'SELECT name FROM project;')
        for val in existing_name:
            if val[0] == name:
                print('The project {} already exists and will not be added to the database.'.format(name))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        project(name, responsible_id)
    VALUES
        (?, ?)
    """
    
    res_exec = database_utils.execute_query(connection, query, 
                                            values = (name, responsible_id))
    
    if res_exec:
        print('The project {} has been succesfully added to the database.'.format(name))
        
        
def add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                      experiment_setup_id, user_id, batch_id, project_id, connection):
    '''
    function to add row to  data table data

    Parameters
    ----------
    mass : float
        mass of the sample in g.
    experiment_no : int
        Number of time the user do the same experiment.
    field : float
        field used for experiemrnt in T (can be None)
    temperature : float
        temmperature used for experiment in K (can be None)
    date: Date
        date when the experiement have been made
    path_import : str
        path to the data to copy and import
    comment : comment 
        comment on the experiement (can be None)
    experiment_setup_id : int
        ID of the experiemental setup used
    user_id : int 
        ID of the user who performed the experiment
    batch_id : int
        ID of the used batch
    project_id : int 
        ID of the project 
    connection : SQL connection.
        Connection to the SQL database

    Returns
    -------
    None.

    '''
    # check that the values are not null 
    if mass is None:
        print('There is no sample mass. Please provide it')
        return None

    if experiment_no is None:
        print('There is no experiment number. Please provide it')
        return None
    

    if date is None:
        print('There is no date for the experiment. Please provide it')
        return None
    
    if path_import is None:
        print('There is no path to retrieve the data. Please provide it')
        return None
    
    if experiment_setup_id is None:
        print('There is no experiement setup id for the data. Please provide it')
        return None
    
    if user_id is None:
        print('There is no user id for the data. Please provide it')
        return None
    
    if batch_id is None:
        print('There is no batch id for the data. Please provide it')
        return None
    
    if project_id is None:
        print('There is no project id for the data. Please provide it')
        return None
    
    # check connection 
    
    if connection is None:
        print('There is no connection to an SQL database. Please initiate it')
        return None
    
    # set teh foreign keys on 
    
    database_utils.execute_query(connection, "PRAGMA foreign_keys = ON;")
    
    # create the pathname of the experimental setup and check that it does not exists  
    # the path is defined as app_rep/project_name/compound_name/batch_name/experiment_type_name/experiment_setup_name
    # and the data name is defined as batch_name_experiement_type_name_experiment_setup_name_user_lastname_field(if exists)_temperature(if exists)_experiment_no_date.
    
    app_rep = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    try:
        project_name = database_utils.fetchall_query(connection, 'SELECT name FROM project WHERE id = {};'.format(project_id))[0][0]
    except IndexError:
        print("The project_id does not exists. Please provide a new one.")
        return None
    
    try:
        compound_id = database_utils.fetchall_query(connection, 'SELECT compound_id FROM batch WHERE id = {};'.format(batch_id))[0][0]
        compound_name = database_utils.fetchall_query(connection, 'SELECT name FROM compound WHERE id = {};'.format(compound_id))[0][0]
        batch_name = database_utils.fetchall_query(connection, 'SELECT name FROM batch WHERE id = {};'.format(batch_id))[0][0]
    except IndexError:
        print("The batch_id does not exists. Please provide a new one.")
        return None
    
    try:
        experiment_type_id = database_utils.fetchall_query(connection, 'SELECT experiment_type_id FROM experiment_setup WHERE id = {};'.format(experiment_setup_id))[0][0]
        experiment_type_name = database_utils.fetchall_query(connection, 'SELECT name FROM experiment_type WHERE id = {};'.format(experiment_type_id))[0][0]
        experiment_setup_name = database_utils.fetchall_query(connection, 'SELECT name FROM experiment_setup WHERE id = {};'.format(experiment_setup_id))[0][0]
    except IndexError:
        print("The experiment_setup_id does not exists. Please provide a new one.")
        return None
    
    try:
        user_lastname = database_utils.fetchall_query(connection, 'SELECT lastname FROM user WHERE id = {};'.format(user_id))[0][0]
    except IndexError:
        print("The user_id does not exists. Please provide a new one.")
        return None


    if field is not None:
        field_name = str(field) + 'T'
    else:
        field_name = ''
    if temperature is not None:
        temp_name = str(temperature) + 'K'
    else:
        temp_name = ''
    date_name = ''.join([date[0:3], date[5:6], date[8:9]])

    # create the filename
    
    new_filename = '_'.join([batch_name, 
                             experiment_type_name, 
                             experiment_setup_name, 
                             user_lastname, 
                             field_name, 
                             temp_name, 
                             str(experiment_no), 
                             date_name]) + '.csv'
    
    
    
    new_path = os.path.join(app_rep,
                            'data',
                            project_name,
                            compound_name,
                            batch_name,
                            experiment_type_name,
                            experiment_setup_name,
                            new_filename)
        
    # check if the data table exists 
    
    res = database_utils.check_table_exists(connection, 'data')
    
    if res == False:
        tables_create.create_data_table(connection)
        print('The data table has been created.')
    
    # if the table exists check that the values you want to add are new 
    
    else:    
   
        existing_path = database_utils.fetchall_query(connection, 'SELECT new_path FROM data;')
        for val in existing_path:
            if val[0] == new_path:
                print('The data {} already exists and will not be added to the database.'.format(new_path))
                return None

    # create the cursor 
        
    query = """
    INSERT INTO 
        data(
            mass,
            experiment_no,
            field, 
            temp,
            date,
            path_import,
            new_path,
            comment, 
            experiment_setup_id,
            user_id,
            batch_id,
            project_id)
    VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    res_exec = database_utils.execute_query(connection, query, 
                                            values = (mass,
                                                      experiment_no,
                                                      field, 
                                                      temperature,
                                                      date,
                                                      path_import,
                                                      new_path,
                                                      comment, 
                                                      experiment_setup_id,
                                                      user_id,
                                                      batch_id,
                                                      project_id))
    
    if res_exec:
        print('The data {} has been succesfully added to the database.'.format(new_path))
    
        # if necessary copy the data form the old path to the new one 
    
        if path_import != new_path:
            
            # create the new path if it does not exists 
        
            if not os.path.exists(new_path):
                os.makedirs(os.path.dirname(new_path))
            
            shutil.copyfile(path_import, new_path)
        
if __name__ == '__main__':
    
    connection = database_utils.create_or_connect_db()
    
    print('\ncreate the first laboratory\n') 
    
    laboratory_name = 'Laboratoire de Physique des Solides'
    university_id = 1
    add_row_laboratory_table(laboratory_name, university_id, connection)
    
    print('\nCreate connection to the database\n')
    
    print('create the first university\n')
    
    university_name = 'Université Paris Saclay'
    university_country = 'France'
    university_city = 'Gif-sur-Yvette'
    university_address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
    add_row_university_table(university_name, university_country, university_city, university_address, connection)
    
    print('\ncheck what happens if we recreate the entry\n') 
    
    add_row_university_table(university_name, university_country, university_city, university_address, connection)
    
    print('\ncreate the second university\n')
    
    university_name = 'Paul Scherrer Institute'
    university_country = "Switzerland"
    university_city = 'Villigen'
    university_address = 'PSI CH, Forschungsstrasse 111, 5232 Villigen'
    add_row_university_table(university_name, university_country, university_city, university_address, connection)
    
    
    print('\ncheck university table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM university;").fetchall())
    cur.close()
    
    print('\ncreate the first laboratory\n') 
    
    laboratory_name = 'Laboratoire de Physique des Solides'
    university_id = 1
    add_row_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n') 
    
    add_row_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncreate the second laboratory\n')
    
    laboratory_name = 'Laboratoire de Physique Théoriques et de Modèles Statistiques'
    university_id = 1
    add_row_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncreate the third laboratory\n') 
    
    laboratory_name = 'Laboratory for Muon Spin Spectroscopy'
    university_id = 2
    add_row_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncheck what happens when the university does not exist\n') 

    laboratory_name = 'Laboratoire test'
    university_id = 3
    add_row_laboratory_table(laboratory_name, university_id, connection)
    
    print('\ncheck laboratory table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM laboratory;").fetchall())
    cur.close()
    
    print('\ncreate the first status\n')
    
    status_name = 'PhD Student'
    add_row_status_table(status_name, connection)
    
    print('\ncreate the second status\n')
    
    status_name = 'Postdoc'
    add_row_status_table(status_name, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    add_row_status_table(status_name, connection)
    
    print('\ncheck status table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM status;").fetchall())
    cur.close()
    
    print('\ncreate the first material type\n')
    
    material_type_name = 'Quantum Spin Liquid'
    add_row_material_type_table(material_type_name, connection)
    
    print('\ncreate the second material type\n')
    
    material_type_name = 'Superconductor'
    add_row_material_type_table(material_type_name, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    add_row_material_type_table(material_type_name, connection)
    
    print('\ncheck material_type table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM material_type;").fetchall())
    cur.close()
    
    print('\ncreate the first compound\n')
    
    compound_name = 'DQVOF'
    compound_formula = '(NH4)2[C7H14N][V7O6F18]'
    material_type_id = 1
    add_row_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    print('\ncreate the second compound\n')
    
    compound_name = 'Herbertsmithite'
    compound_formula = 'ZnCu3(OH)6Cl2'
    material_type_id = 1
    add_row_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    add_row_compound_table(compound_name, compound_formula, material_type_id, connection)
     
    print('\ncreate the third compound\n')
    
    compound_name = 'YBACUO'
    compound_formula = 'YBa2Cu3O7'
    material_type_id = 2
    add_row_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    print('Test compound without material type')
    compound_name = 'test'
    compound_formula = 'test'
    material_type_id = 3
    add_row_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    print('\ncheck compound table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM compound;").fetchall())
    cur.close()
    
    print('\ncreate the first experiement type\n')
    
    experiment_type_name = 'Heat Capacity vs Temperature'
    add_row_experiment_type_table(experiment_type_name, connection)
    
    print('\ncreate the second experiement type\n')
    
    experiment_type_name = 'Magnetization vs Temperature'
    add_row_experiment_type_table(experiment_type_name, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    add_row_experiment_type_table(experiment_type_name, connection)
    
    print('\ncheck experiment_type table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM experiment_type;").fetchall())
    cur.close()
    
    print('\ncreate the first user\n')
    
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 1
    laboratory_id = 1
    add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\ncreate the second user\n')
    
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 2
    laboratory_id = 3
    add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\ncreate the third user\n')
    
    user_firstname = 'Gediminas'
    user_lastname = 'Simutis'
    status_id = 2
    laboratory_id = 3
    add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\nTest user without status id.\n')
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 3
    laboratory_id = 2
    add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    print('\nTest user without laboratory id.\n')
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 2
    laboratory_id = 4
    add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
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
    add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
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
    add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                    max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
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
    add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
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
    add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                    max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    print('\ncheck experiment setup table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM experiment_setup;").fetchall())
    cur.close()
    
    print('\nCreate the first batch')
    batch_name = "DQVOF 1"
    mass = 100
    color = 'green'
    Type = "powder"
    creation_date = '2019-10-12'
    compound_id = 1
    grower_id = 1
    add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)
    
    
    print('\nCreate the second batch')
    batch_name = "Test 2002"
    mass = 200
    color = 'green'
    Type = "single cristal"
    creation_date = '2017-10-12'
    compound_id = 2
    grower_id = 3
    add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)
    
    print('\nCheck wrong batch type\n')
    
    batch_name = "Test wrong batch type"
    mass = 200
    color = 'green'
    Type = "test"
    creation_date = '2017-10-12'
    compound_id = 2
    grower_id = 3
    add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)
    
    print('\nCheck worng compound.')
    batch_name = "Test wrong compound"
    mass = 200
    color = 'green'
    Type = "single cristal"
    creation_date = '2017-10-12'
    compound_id = 5
    grower_id = 3
    add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)
    
    print('\nCheck wrong grower.')
    batch_name = "Test wrong grower"
    mass = 200
    color = 'green'
    Type = "single cristal"
    creation_date = '2017-10-12'
    compound_id = 2
    grower_id = 6
    add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)
    
    print('\ncheck batch table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM batch;").fetchall())
    cur.close()
    
    print('\nCreate the first project\n')
    project_name = "Super project"
    project_responsible_id = 1
    add_row_project_table(project_name, project_responsible_id, connection)
    
    print('\nCreate the second project\n')
    project_name = "Super other project"
    project_responsible_id = 3
    add_row_project_table(project_name, project_responsible_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    
    add_row_project_table(project_name, project_responsible_id, connection)
    
    print("\nCheck wrong responsible id\n")
    
    project_name = "test wrong responsible"
    project_responsible_id = 7
    add_row_project_table(project_name, project_responsible_id, connection)
    
    print('\ncheck project table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM project;").fetchall())
    cur.close()
    
    print('\nCreate the first data\n')
    
    mass = 100
    experiment_no = 1
    field = 2 
    temperature = 300 
    date = '2018-01-21'
    path_import = 'D:\\Travail\\PSI\\BackUpFeb2019\\MuSR_Project_Jco\\Experiment\\Squid\\ImVOF\\PyzVOF\\PyzVOFZFCFC1T.dc.dat'
    comment = None
    experiment_setup_id = 1
    user_id = 1
    batch_id = 1
    project_id = 1
    
    add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)
    
    
    print('\nCreate the second data\n')
    
    mass = 150
    experiment_no = 5
    field = None 
    temperature = None 
    date = '2018-12-21'
    path_import = 'D:\\Travail\\PSI\\BackUpFeb2019\\MuSR_Project_Jco\\Experiment\\Squid\\ImVOF\\PyzVOF\\PyzVOFZFCFC1T.dc.dat'
    comment = None
    experiment_setup_id = 2
    user_id = 3
    batch_id = 1
    project_id = 2
    
    add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)
    
    print('\ncheck what happens if we recreate the entry\n')
    
    add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)
    
    print('\nCheck wrong experiement_setup\n')
    
    mass = 150
    experiment_no = 5
    field = None 
    temperature = None 
    date = '2018-12-21'
    path_import = 'D:\\Travail\\PSI\\BackUpFeb2019\\MuSR_Project_Jco\\Experiment\\Squid\\ImVOF\\PyzVOF\\PyzVOFZFCFC1T.dc.dat'
    comment = None
    experiment_setup_id = 5
    user_id = 3
    batch_id = 1
    project_id = 2
    
    add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)
    
    print('\nCheck wrong user\n')
    
    mass = 150
    experiment_no = 5
    field = None 
    temperature = None 
    date = '2018-12-21'
    path_import = 'D:\\Travail\\PSI\\BackUpFeb2019\\MuSR_Project_Jco\\Experiment\\Squid\\ImVOF\\PyzVOF\\PyzVOFZFCFC1T.dc.dat'
    comment = None
    experiment_setup_id = 1
    user_id = 7
    batch_id = 1
    project_id = 2
    
    add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)


    print('\nCheck wrong batch\n')
    
    mass = 150
    experiment_no = 5
    field = None 
    temperature = None 
    date = '2018-12-21'
    path_import = 'D:\\Travail\\PSI\\BackUpFeb2019\\MuSR_Project_Jco\\Experiment\\Squid\\ImVOF\\PyzVOF\\PyzVOFZFCFC1T.dc.dat'
    comment = None
    experiment_setup_id = 1
    user_id = 3
    batch_id = 10
    project_id = 2
    
    add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)


    print('\nCHeck wrong project\n')
    
    mass = 150
    experiment_no = 5
    field = None 
    temperature = None 
    date = '2018-12-21'
    path_import = 'D:\\Travail\\PSI\\BackUpFeb2019\\MuSR_Project_Jco\\Experiment\\Squid\\ImVOF\\PyzVOF\\PyzVOFZFCFC1T.dc.dat'
    comment = None
    experiment_setup_id = 1
    user_id = 3
    batch_id = 1
    project_id = 15
    
    add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)

    print('\ncheck data table values\n')
    
    cur = connection.cursor()
    print(cur.execute("SELECT * FROM data;").fetchall())
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
    print(cur.execute("SELECT * FROM batch;").fetchall())
    print(cur.execute("SELECT * FROM project;").fetchall())
    print(cur.execute("SELECT * FROM data;").fetchall())
    cur.close()
    
    # print('\nCheck delete row for university\n')
    
    database_utils.delete_id_from_table(connection, 'university', 1)
   
    
   
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
    print(cur.execute("SELECT * FROM batch;").fetchall())
    print(cur.execute("SELECT * FROM project;").fetchall())
    print(cur.execute("SELECT * FROM data;").fetchall())
    cur.close()
    
    
    # close the connection
    connection.close()