'''
test module for tables_create module
'''

import pytest

import CollaSci.db_function.tables_create as tables_create
import CollaSci.db_function.database_utils as database_utils

# create an empty connection with foreign_keys on 

@pytest.fixture()
def empty_db(tmp_path):
    '''
    Fixture to create the empty db if it does not exists
    
    Returns
    -------
    None
    '''   

class TestCreate_university_table():
    '''
    Class to test the create_university_table function
    '''
    def test_create_university_table_no_connection(self, capsys):
 
        connection = None
        tables_create.create_university_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_university_table(self, tmp_path):
       
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)

        # create the table 
        tables_create.create_university_table(connection)
             
        ret_uni = database_utils.check_table_exists(connection, 'university')
        ret_user = database_utils.check_table_exists(connection, 'user')
        connection.close()
        
        assert ret_uni == True
        assert ret_user == False
        
class TestCreate_laboratory_table():
    '''
    Class to test the create_laboratory_table function
    '''
    def test_create_laboratory_table_no_connection(self, capsys):
        connection = None
        tables_create.create_laboratory_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_laboratory_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_laboratory_table(connection)
        
        ret_labo = database_utils.check_table_exists(connection, 'laboratory')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_labo == True
        assert ret_user == False
        
class TestCreate_status_table():
    '''
    Class to test the create_status_table function
    '''
    def test_create_status_table_no_connection(self, capsys):
        connection = None
        tables_create.create_status_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_status_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_status_table(connection)
        
        ret_status = database_utils.check_table_exists(connection, 'status')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_status == True
        assert ret_user == False


class TestCreate_material_type_table():
    '''
    Class to test the create_material_type_table function
    '''
    def test_create_material_type_table_no_connection(self, capsys):
        connection = None
        tables_create.create_material_type_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_material_type_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_material_type_table(connection)
        
        ret_material_type = database_utils.check_table_exists(connection, 'material_type')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_material_type == True
        assert ret_user == False

class TestCreate_compound_table():
    '''
    Class to test the create_compound_table function
    '''
    def test_create_compound_table_no_connection(self, capsys):
        connection = None
        tables_create.create_compound_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_compound_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_compound_table(connection)
        
        ret_compound = database_utils.check_table_exists(connection, 'compound')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_compound == True
        assert ret_user == False

class TestCreate_experiment_type_table():
    def test_create_experiment_type_table_no_connection(self, capsys):
        connection = None
        tables_create.create_experiment_type_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_experiment_type_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_experiment_type_table(connection)
        
        ret_experiment_type = database_utils.check_table_exists(connection, 'experiment_type')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_experiment_type == True
        assert ret_user == False

class TestCreate_user_table():
    '''
    Class to test the create_user_table function
    '''
    def test_create_user_table_no_connection(self, capsys):
        connection = None
        tables_create.create_user_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_user_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_user_table(connection)
        
        ret_user = database_utils.check_table_exists(connection, 'user')
        ret_labo = database_utils.check_table_exists(connection, 'laboratory')

        connection.close()
        
        assert ret_user == True
        assert ret_labo == False

class TestCreate_experiment_setup_table():
    '''
    Class to test the create_experiment_setup_table function
    '''
    def test_create_experiment_setup_table_no_connection(self, capsys):
        connection = None
        tables_create.create_experiment_setup_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_experiment_setup_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_experiment_setup_table(connection)
        
        ret_experiment_setup = database_utils.check_table_exists(connection, 'experiment_setup')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_experiment_setup == True
        assert ret_user == False

class TestCreate_batch_table():
    '''
    Class to test the create_batch_table function
    '''
    def test_create_batch_table_no_connection(self, capsys):
        connection = None
        tables_create.create_batch_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_batch_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_batch_table(connection)
        
        ret_batch = database_utils.check_table_exists(connection, 'batch')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_batch == True
        assert ret_user == False

class TestCreate_project_table():
    '''
    Class to test the create_project_table function
    '''
    def test_create_project_table_no_connection(self, capsys):
        connection = None
        tables_create.create_project_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_project_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_project_table(connection)
        
        ret_project = database_utils.check_table_exists(connection, 'project')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_project == True
        assert ret_user == False

class TestCreate_data_table():
    '''
    Class to test the create_data_table function
    '''
    def test_create_data_table_no_connection(self, capsys):
        connection = None
        tables_create.create_data_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_data_table(self, tmp_path):
        
        # create an empty connection with foreign keys ON
        name = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name)
       
        # create the table 
        tables_create.create_data_table(connection)
        
        ret_data = database_utils.check_table_exists(connection, 'data')
        ret_user = database_utils.check_table_exists(connection, 'user')

        connection.close()
        
        assert ret_data == True
        assert ret_user == False