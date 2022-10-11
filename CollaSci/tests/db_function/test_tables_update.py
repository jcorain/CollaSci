'''
test module for tables_update module
'''
import pytest

import CollaSci.db_function.tables_create as tables_create
import CollaSci.db_function.tables_update as tables_update
import CollaSci.db_function.database_utils as database_utils

class TestAdd_row_university_table():
    '''
    Class to test the add row function for the university table 
    '''
    def test_add_row_univeersity_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        name = 'Université Paris Saclay'
        country = 'France'
        city = 'Gif-sur-Yvette'
        address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
        connection = None
        
        res = tables_update.add_row_university_table(name, country, city,address, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None
        
    def test_add_row_univeersity_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        country = 'France'
        city = 'Gif-sur-Yvette'
        address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
        
        res = tables_update.add_row_university_table(name, country, city,address, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no university name. Please provide it' in captured.out
        
        assert res == None

    def test_add_row_univeersity_no_country(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Université Paris Saclay'
        country = None
        city = 'Gif-sur-Yvette'
        address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
        
        res = tables_update.add_row_university_table(name, country, city,address, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no university country. Please provide it' in captured.out
        
        assert res == None        

    def test_add_row_univeersity_no_city(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no city 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Université Paris Saclay'
        country = 'France'
        city = None
        address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
        
        res = tables_update.add_row_university_table(name, country, city,address, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no university city. Please provide it' in captured.out
        
        assert res == None    
        
    def test_add_row_univeersity_no_address(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no address
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Université Paris Saclay'
        country = 'France'
        city = 'Gif-sur-Yvette'
        address = None
        
        res = tables_update.add_row_university_table(name, country, city,address, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no university address. Please provide it' in captured.out
        
        assert res == None

    def test_add_row_univeersity_new_table(self, capsys, tmp_path):
        '''
        function to test the behavior of add row for university table when there is no existing university table
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        # get the new values 
        name = 'Université Paris Saclay'
        country = 'France'
        city = 'Gif-sur-Yvette'
        address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
        
        tables_update.add_row_university_table(name, country, city,address, connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM university')
                
        assert 'The university table has been created.' in captured.out
        assert 'The university {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1, 'Université Paris Saclay', 
                                    'France',
                                    'Gif-sur-Yvette', 
                                    'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France')]
    
    def test_add_row_univeersity_same_values(self, capsys, tmp_path):
        '''
        function to test the behavior of add row for university table when there is no existing university table
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        # get the new values 
        name = 'Université Paris Saclay'
        country = 'France'
        city = 'Gif-sur-Yvette'
        address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
        
        tables_update.add_row_university_table(name, country, city,address, connection)
        
        # recreate the same data 
        country = 'test'
        city = 'test'
        address = 'test'
        
        tables_update.add_row_university_table(name, country, city,address, connection)
       
        captured = capsys.readouterr()
         
        assert 'The university {} already exists and will not be added to the database.'.format(name) in captured.out
        
    def test_add_row_univeersity_two_rows(self, capsys, tmp_path):
        '''
        function to test the behavior of add row for university table when there is no existing university table
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        # get the new values 
        name = 'Université Paris Saclay'
        country = 'France'
        city = 'Gif-sur-Yvette'
        address = 'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'
        
        tables_update.add_row_university_table(name, country, city,address, connection)
        
        # get the new values 
        
        name = 'Paul Scherrer Institute'
        country = "Switzerland"
        city = 'Villigen'
        address = 'PSI CH, Forschungsstrasse 111, 5232 Villigen'
        
        tables_update.add_row_university_table(name, country, city,address, connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM university')
                
        assert 'The university table has been created.' in captured.out
        assert 'The university {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1, 
                                    'Université Paris Saclay', 
                                    'France',
                                    'Gif-sur-Yvette', 
                                    'Bâtiment Bréguet, 3 Rue Joliot Curie 2e ét, 91190 Gif-sur-Yvette, France'),
                                   (2, 
                                    'Paul Scherrer Institute',
                                    'Switzerland', 
                                    'Villigen',
                                    'PSI CH, Forschungsstrasse 111, 5232 Villigen')]     

class TestAdd_row_laboratory_table():
    '''
    Class to test the add row function for the laboratory table 
    '''
    def test_add_row_laboratory_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        name = 'Laboratoire de Physique des Solides'
        university_id = 1
        connection = None
        
        res = tables_update.add_row_laboratory_table(name, university_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None
        
    def test_add_row_laboratory_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        university_id = 1
        
        res = tables_update.add_row_laboratory_table(name, university_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no laboratory name. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_laboratory_no_university_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no university_id 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Laboratoire de Physique des Solides'
        university_id = None
        
        res = tables_update.add_row_laboratory_table(name, university_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no university_id. Please provide it' in captured.out
        
        assert res == None
    
    def test_add_row_laboratory_no_university_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no university table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Laboratoire de Physique des Solides'
        university_id = 1
        
        tables_update.add_row_laboratory_table(name, university_id, connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM laboratory')
        
        assert "The error 'no such table: main.university' occurred" in captured.out
        assert existing_values == []
        
    def test_add_row_laboratory_new_table(self, capsys, create_example_db_university):
        '''
        function to test the behavior of the function when adding new table
        '''
        
        connection =  create_example_db_university
        
        name = 'Laboratoire de Physique des Solides'
        university_id = 1
        
        tables_update.add_row_laboratory_table(name, university_id, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM laboratory')
        
        assert 'The laboratory table has been created.' in captured.out
        assert 'The laboratory {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'Laboratoire de Physique des Solides', 
                                    1)]

    def test_add_row_laboratory_same_values(self, capsys, create_example_db_university):
        '''
        function to test the behavior of the function when getting same laboratory name
        '''
        
        connection =  create_example_db_university
        
        name = 'Laboratoire de Physique des Solides'
        university_id = 1
        
        
        tables_update.add_row_laboratory_table(name, university_id, connection)
        
        # recretae the same data 
        
        university_id = 2
        
        tables_update.add_row_laboratory_table(name, university_id, connection)
        
        captured = capsys.readouterr()
                
        
        assert 'The laboratory {} already exists and will not be added to the database.'.format(name) in captured.out


    def test_add_row_laboratory_three_rows(self, capsys, create_example_db_university):
        '''
        function to test the behavior of the function with different rows
        '''
        
        connection =  create_example_db_university
        
        name = 'Laboratoire de Physique des Solides'
        university_id = 1
        
        tables_update.add_row_laboratory_table(name, university_id, connection)
        
        name = 'Laboratoire de Physique Théoriques et de Modèles Statistiques'
        university_id = 1
        
        tables_update.add_row_laboratory_table(name, university_id, connection)
        
        name = 'Laboratory for Muon Spin Spectroscopy'
        university_id = 2
        tables_update.add_row_laboratory_table(name, university_id, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM laboratory')
        
        assert 'The laboratory table has been created.' in captured.out
        assert 'The laboratory {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'Laboratoire de Physique des Solides', 
                                    1),
                                   (2,
                                    'Laboratoire de Physique Théoriques et de Modèles Statistiques', 
                                    1),
                                   (3,
                                    'Laboratory for Muon Spin Spectroscopy', 
                                    2)]
        
class TestAdd_row_status_table():
    '''
    Class to test the add row function for the status table 
    '''
    def test_add_row_status_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        name = 'PhD Student'
        connection = None
        
        res = tables_update.add_row_status_table(name, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None
        
    def test_add_row_status_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        
        res = tables_update.add_row_status_table(name, connection)
       
        captured = capsys.readouterr()
        
        assert 'There is no status name. Please provide it' in captured.out
        
        assert res == None
        
  
    def test_add_row_status_new_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'PhD Student'
        
        tables_update.add_row_status_table(name, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM status')
        
        assert 'The status table has been created.' in captured.out
        assert 'The status {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'PhD Student')]
        
    def test_add_row_status_same_values(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'PhD Student'
        
        tables_update.add_row_status_table(name, connection)
        
        # recreate the data 
        tables_update.add_row_status_table(name, connection)
        
        
        captured = capsys.readouterr()
                
        assert 'The status {} already exists and will not be added to the database.'.format(name) in captured.out

    def test_add_row_status_two_rows(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'PhD Student'
        tables_update.add_row_status_table(name, connection)
        
        name = 'PostDoc'
        tables_update.add_row_status_table(name, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM status')
        
        assert 'The status table has been created.' in captured.out
        assert 'The status {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'PhD Student'),
                                   (2,
                                    'PostDoc')]
