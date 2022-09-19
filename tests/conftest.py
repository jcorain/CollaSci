'''
module for test configuration
'''

import pytest
import os

import CollaSci.db_function.database_utils as database_utils
import CollaSci.db_function.tables_update as tables_update


@pytest.fixture(scope = "session")
def create_example_db():
    '''
    Fixture to create the exmaple db if it does not exists
    
    Returns
    -------
    None
    '''
    
    path = os.path.join(os.path.dirname(__file__), 'data')
    name = 'database_test.sqlite'
    connection = database_utils.create_or_connect_db(path, name)
    
    # print('create the first university\n')
    
    university_name = 'Université Paris Saclay'
    university_country = 'France'
    university_city = 'Gif-sur-Yvette'
    university_address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
    tables_update.add_row_university_table(university_name, university_country, university_city, university_address, connection)
    
    # print('\ncreate the second university\n')
    
    university_name = 'Paul Scherrer Institute'
    university_country = "Switzerland"
    university_city = 'Villigen'
    university_address = 'PSI CH, Forschungsstrasse 111, 5232 Villigen'
    tables_update.add_row_university_table(university_name, university_country, university_city, university_address, connection)
    
   
    # print('\ncreate the first laboratory\n') 
    
    laboratory_name = 'Laboratoire de Physique des Solides'
    university_id = 1
    tables_update.add_row_laboratory_table(laboratory_name, university_id, connection)
    
    # print('\ncreate the second laboratory\n')
    
    laboratory_name = 'Laboratoire de Physique Théoriques et de Modèles Statistiques'
    university_id = 1
    tables_update.add_row_laboratory_table(laboratory_name, university_id, connection)
    
    # print('\ncreate the third laboratory\n') 
    
    laboratory_name = 'Laboratory for Muon Spin Spectroscopy'
    university_id = 2
    tables_update.add_row_laboratory_table(laboratory_name, university_id, connection)
    
    
    # print('\ncreate the first status\n')
    
    status_name = 'PhD Student'
    tables_update.add_row_status_table(status_name, connection)
    
    # print('\ncreate the second status\n')
    
    status_name = 'Postdoc'
    tables_update.add_row_status_table(status_name, connection)
    
    
    # print('\ncreate the first material type\n')
    
    material_type_name = 'Quantum Spin Liquid'
    tables_update.add_row_material_type_table(material_type_name, connection)
    
    # print('\ncreate the second material type\n')
    
    material_type_name = 'Superconductor'
    tables_update.add_row_material_type_table(material_type_name, connection)
    
    
    # print('\ncreate the first compound\n')
    
    compound_name = 'DQVOF'
    compound_formula = '(NH4)2[C7H14N][V7O6F18]'
    material_type_id = 1
    tables_update.add_row_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    # print('\ncreate the second compound\n')
    
    compound_name = 'Herbertsmithite'
    compound_formula = 'ZnCu3(OH)6Cl2'
    material_type_id = 1
    tables_update.add_row_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    # print('\ncreate the third compound\n')
    
    compound_name = 'YBACUO'
    compound_formula = 'YBa2Cu3O7'
    material_type_id = 2
    tables_update.add_row_compound_table(compound_name, compound_formula, material_type_id, connection)
    
    
    # print('\ncreate the first experiement type\n')
    
    experiment_type_name = 'Heat Capacity vs Temperature'
    tables_update.add_row_experiment_type_table(experiment_type_name, connection)
    
    # print('\ncreate the second experiement type\n')
    
    experiment_type_name = 'Magnetization vs Temperature'
    tables_update.add_row_experiment_type_table(experiment_type_name, connection)
    
    
    # print('\ncreate the first user\n')
    
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 1
    laboratory_id = 1
    tables_update.add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    # print('\ncreate the second user\n')
    
    user_firstname = 'Jean-Christophe'
    user_lastname = 'Orain'
    status_id = 2
    laboratory_id = 3
    tables_update.add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)
    
    # print('\ncreate the third user\n')
    
    user_firstname = 'Gediminas'
    user_lastname = 'Simutis'
    status_id = 2
    laboratory_id = 3
    tables_update.add_row_user_table(user_firstname, user_lastname, status_id, laboratory_id, connection)

    
    # print('\ncreate the first experimental setup\n')
    
    experimental_setup_name = 'MMPS He4'
    roomname = 'Salon'
    experimental_setup_start_date = '25/05/2018'
    min_field = 0
    max_field = 5
    min_temperature = 1.5
    max_temperature = 300
    experiment_type_id = 1
    responsible_id = 1
    tables_update.add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                    max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    # print('\ncreate the second experimental setup\n')
    
    experimental_setup_name = 'MMPS He4 bis'
    roomname = 'Salon'
    experimental_setup_start_date = '25/05/2018'
    min_field = None
    max_field = None
    min_temperature = None
    max_temperature = None
    experiment_type_id = 1
    responsible_id = 2
    tables_update.add_row_experiment_setup_table(experimental_setup_name, roomname, experimental_setup_start_date, min_field, 
                                    max_field, min_temperature, max_temperature, experiment_type_id, responsible_id, connection)
    
    
    # print('\nCreate the first batch')
    batch_name = "DQVOF 1"
    mass = 100
    color = 'green'
    Type = "powder"
    creation_date = '2019-10-12'
    compound_id = 1
    grower_id = 1
    tables_update.add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)
    
    
    # print('\nCreate the second batch')
    batch_name = "Test 2002"
    mass = 200
    color = 'green'
    Type = "single cristal"
    creation_date = '2017-10-12'
    compound_id = 2
    grower_id = 3
    tables_update.add_row_batch_table(batch_name, mass, color, Type, creation_date, compound_id, grower_id, connection)
    
    
    
    # print('\nCreate the first project\n')
    project_name = "Super project"
    project_responsible_id = 1
    tables_update.add_row_project_table(project_name, project_responsible_id, connection)
    
    # print('\nCreate the second project\n')
    project_name = "Super other project"
    project_responsible_id = 3
    tables_update.add_row_project_table(project_name, project_responsible_id, connection)
    
    
    # print('\nCreate the first data\n')
    
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
    
    tables_update.add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)
    
    
    # print('\nCreate the second data\n')
    
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
    
    tables_update.add_row_data_table(mass, experiment_no, field, temperature, date, path_import, comment, 
                          experiment_setup_id, user_id, batch_id, project_id, connection)
    
    # close the connection
    connection.close()

# get the database name and path as a fixture
@pytest.fixture(scope = 'session')
def example_connection_path_name(create_example_db):
    '''
    pytest fixture to get the path and name connection to the test database 
    situated in test/data/database_test.sqlite
    Returns
    -------
    path and name to the test connection 
    '''
    path = os.path.join(os.path.dirname(__file__), 'data')
    name = 'database_test.sqlite'
    
    # if the database does not exist create it
    if not os.path.isfile(os.path.join(path, name)):
        print('test')
        create_example_db
        
    return path, name

@pytest.fixture(scope = 'session')
def example_connection(create_example_db):
    '''
    Fixture to create a connection to the database test connection

    Returns
    -------
    SQLITE connection.

    '''
    path = os.path.join(os.path.dirname(__file__), 'data')
    name = 'database_test.sqlite'
    
    # if the database does not exist create it
    if not os.path.isfile(os.path.join(path, name)):
        create_example_db
    
    connection = database_utils.create_or_connect_db(path = path, name = name)
    return connection