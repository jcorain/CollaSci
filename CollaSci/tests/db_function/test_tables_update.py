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
        
    def test_add_row_laboratory_wrong_university_id(self, capsys, create_example_db_university):
        '''
        function to test the behavior of the function when adding new table
        '''
        
        connection =  create_example_db_university
        
        name = 'Laboratoire de Physique des Solides'
        university_id = 3
        
        tables_update.add_row_laboratory_table(name, university_id, connection)
        
        captured = capsys.readouterr()
          
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM laboratory')
                
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []
        
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

class TestAdd_row_material_type_table():
    '''
    Class to test the add row function for the material type table 
    '''
    def test_add_row_material_type_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        name = 'Quantum Spin Liquid'
        connection = None
        
        res = tables_update.add_row_material_type_table(name, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None
        
    def test_add_row_material_type_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        
        res = tables_update.add_row_material_type_table(name, connection)
       
        captured = capsys.readouterr()
        
        assert 'There is no material type name. Please provide it' in captured.out
        
        assert res == None
        
  
    def test_add_row_material_type_new_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Quantum Spin Liquid'
        
        tables_update.add_row_material_type_table(name, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM material_type')
        
        assert 'The material_type table has been created.' in captured.out
        assert 'The material_type {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'Quantum Spin Liquid')]
        
    def test_add_row_material_type_same_values(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Quantum Spin Liquid'
        
        tables_update.add_row_material_type_table(name, connection)
        
        # recreate the data 
        tables_update.add_row_material_type_table(name, connection)
        
        
        captured = capsys.readouterr()
                
        assert 'The material_type {} already exists and will not be added to the database.'.format(name) in captured.out

    def test_add_row_material_type_two_rows(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Quantum Spin Liquid'
        tables_update.add_row_material_type_table(name, connection)
        
        name = 'Superconductor'
        tables_update.add_row_material_type_table(name, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM material_type')
        
        assert 'The material_type table has been created.' in captured.out
        assert 'The material_type {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'Quantum Spin Liquid'),
                                   (2,
                                    'Superconductor')]

class TestAdd_row_compound_table():
    '''
    Class to test the add row function for the compound table 
    '''
    def test_add_row_compound_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        name = 'DQVOF'
        formula = '(NH4)2[C7H14N][V7O6F18]'
        material_type_id = 1
        connection = None
        
        res = tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None
        
    def test_add_row_compound_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        formula = '(NH4)2[C7H14N][V7O6F18]'
        material_type_id = 1
        
        res = tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no compound name. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_compound_no_formula(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no formula 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'DQVOF'
        formula = None
        material_type_id = 1
        
        res = tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no compound formula. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_compound_no_material_type_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no material_type_id 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'DQVOF'
        formula = '(NH4)2[C7H14N][V7O6F18]'
        material_type_id = None
        
        res = tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no material_type_id. Please provide it' in captured.out
        
        assert res == None        

    
    def test_add_row_compound_no_material_type_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no material_type table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'DQVOF'
        formula = '(NH4)2[C7H14N][V7O6F18]'
        material_type_id = 1
        
        tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM compound')
        
        assert "The error 'no such table: main.material_type' occurred" in captured.out
        assert existing_values == []
        
    def test_add_row_compound_new_table(self, capsys, create_example_db_material_type):
        '''
        function to test the behavior of the function when adding new table
        '''
        
        connection =  create_example_db_material_type
        
        name = 'DQVOF'
        formula = '(NH4)2[C7H14N][V7O6F18]'
        material_type_id = 1
        
        tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM compound')
        
        assert 'The compound table has been created.' in captured.out
        assert 'The compound {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'DQVOF', 
                                    '(NH4)2[C7H14N][V7O6F18]',
                                    1)]

    def test_add_row_compound_same_values(self, capsys, create_example_db_material_type):
        '''
        function to test the behavior of the function when getting same laboratory name
        '''
        
        connection =  create_example_db_material_type
        
        name = 'DQVOF'
        formula = '(NH4)2[C7H14N][V7O6F18]'
        material_type_id = 1
        
        tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        # recretae the same data 
        
        formula = '(NH4)2[C7H14N][V7O6F18]bis'
        material_type_id = 2
        
        tables_update.add_row_compound_table(name, formula, material_type_id, connection)

        
        captured = capsys.readouterr()
                
        
        assert 'The compound {} already exists and will not be added to the database.'.format(name) in captured.out


    def test_add_row_compound_three_rows(self, capsys, create_example_db_material_type):
        '''
        function to test the behavior of the function with different rows
        '''
        
        connection =  create_example_db_material_type
        
        name = 'DQVOF'
        formula = '(NH4)2[C7H14N][V7O6F18]'
        material_type_id = 1
        
        tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        name = 'Herbertsmithite'
        formula = 'ZnCu3(OH)6Cl2'
        material_type_id = 1
        
        tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        name = 'YBACUO'
        formula = 'YBa2Cu3O7'
        material_type_id = 2
        
        tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM compound')
                
        assert 'The compound table has been created.' in captured.out
        assert 'The compound {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'DQVOF', 
                                    '(NH4)2[C7H14N][V7O6F18]',
                                    1),
                                    (2,
                                    'Herbertsmithite', 
                                    'ZnCu3(OH)6Cl2',
                                    1),
                                    (3,
                                    'YBACUO', 
                                    'YBa2Cu3O7',
                                    2)]
    
    def test_add_row_compound_wrong_material_type_id(self, capsys, create_example_db_material_type):
        '''
        function to test the behavior of the function when adding new table
        '''
        
        connection =  create_example_db_material_type
        
        name = 'DQVOF'
        formula = '(NH4)2[C7H14N][V7O6F18]'
        material_type_id = 3
        
        tables_update.add_row_compound_table(name, formula, material_type_id, connection)
        
        captured = capsys.readouterr()
          
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM compound')
                
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []
        
class TestAdd_row_experiment_type_table():
    '''
    Class to test the add row function for the experiment type table 
    '''
    def test_add_row_experiment_type_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        name = 'Heat Capacity vs Temperature'
        connection = None
        
        res = tables_update.add_row_experiment_type_table(name, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None
        
    def test_add_row_experiment_type_type_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        
        res = tables_update.add_row_experiment_type_table(name, connection)
       
        captured = capsys.readouterr()
        
        assert 'There is no experiment type name. Please provide it' in captured.out
        
        assert res == None
        
  
    def test_add_row_experiment_type_new_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Heat Capacity vs Temperature'
        
        tables_update.add_row_experiment_type_table(name, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_type')
        
        assert 'The experiment_type table has been created.' in captured.out
        assert 'The experiment_type {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'Heat Capacity vs Temperature')]
        
    def test_add_row_experiment_type_same_values(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Heat Capacity vs Temperature'
        
        tables_update.add_row_experiment_type_table(name, connection)
        
        # recreate the data 
        tables_update.add_row_experiment_type_table(name, connection)
        
        
        captured = capsys.readouterr()
                
        assert 'The experiment_type {} already exists and will not be added to the database.'.format(name) in captured.out

    def test_add_row_experiment_type_two_rows(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when creating new table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'Heat Capacity vs Temperature' 
        tables_update.add_row_experiment_type_table(name, connection)
        
        name = 'Magnetization vs Temperature'
        tables_update.add_row_experiment_type_table(name, connection)
        
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_type')
        
        assert 'The experiment_type table has been created.' in captured.out
        assert 'The experiment_type {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'Heat Capacity vs Temperature'),
                                   (2,
                                    'Magnetization vs Temperature')]
        
        
class TestAdd_row_user_table():
    '''
    Class to test the add row function for the user table 
    '''
    def test_add_row_user_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 1
        laboratory_id = 1
        connection = None
        
        res = tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None
        
    def test_add_row_user_no_firstname(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        firstname = None
        lastname = 'Orain'
        status_id = 1
        laboratory_id = 1
        
        res = tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no user firstname. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_user_no_lastname(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no lastname 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        firstname = 'Jean-Christophe'
        lastname = None
        status_id = 1
        laboratory_id = 1
        
        res = tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no user lastname. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_user_no_status_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no status_id 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = None
        laboratory_id = 1
        
        res = tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no status_id. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_user_no_laboratory_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no laboratory_id 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 1
        laboratory_id = None
        
        res = tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no laboratory_id. Please provide it' in captured.out
        
        assert res == None

    def test_add_row_user_no_laboratory_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no status table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 1
        laboratory_id = 1
        
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM user')
        
        assert "The error 'no such table: main.laboratory' occurred" in captured.out
        assert existing_values == []    
        
    def test_add_row_user_no_status_table(self, capsys, create_example_db_laboratory):
        '''
        function to test the behavior of the function when there is no status table 
        '''
        
        connection = create_example_db_laboratory
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 1
        laboratory_id = 1
        
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM user')
        
        assert "The error 'no such table: main.status' occurred" in captured.out
        assert existing_values == []    
    
    def test_add_row_user_new_table(self, capsys, create_example_db_laboratory_status):
        '''
        function to test the behavior of the function when adding new table
        '''
        
        connection =  create_example_db_laboratory_status
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 1
        laboratory_id = 1
        
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        laboratory_name = database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(laboratory_id))[0][0]
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM user')
        
        assert 'The user table has been created.' in captured.out
        assert 'The user {} {} ({}) has been succesfully added to the database.'.format(firstname, lastname, laboratory_name) in captured.out
        assert existing_values == [(1,
                                    'Jean-Christophe',
                                    'Orain',
                                    1,
                                    1)]
        
    def test_add_row_user_same_values(self, capsys, create_example_db_laboratory_status):
        '''
        function to test the behavior of the function when getting same laboratory name
        '''
        
        connection =  create_example_db_laboratory_status
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 1
        laboratory_id = 1
        
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
         
        # recretae the same data 
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 2
        laboratory_id = 1
        
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        laboratory_name = database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(laboratory_id))[0][0]
        
        captured = capsys.readouterr()      
        assert 'The user {} {} ({}) already exists and will not be added to the database.'.format(firstname, lastname, laboratory_name) in captured.out

    def test_add_row_user_wrong_laboratory_id(self, capsys, create_example_db_laboratory_status):
        '''
        function to test the behavior of the function when having wrong laboratory id
        '''
        
        connection =  create_example_db_laboratory_status
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 1
        laboratory_id = 5
        
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
              
        captured = capsys.readouterr()      
          
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM user')
                
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []
        
    def test_add_row_user_wrong_status_id(self, capsys, create_example_db_laboratory_status):
        '''
        function to test the behavior of the function when having wrong status id
        '''
        
        connection =  create_example_db_laboratory_status
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 5
        laboratory_id = 1
        
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
              
        captured = capsys.readouterr()      
          
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM user')
                
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []

    def test_add_row_user_three_rows(self, capsys, create_example_db_laboratory_status):
        '''
        function to test the behavior of the function with different rows
        '''
        
        connection =  create_example_db_laboratory_status
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 1
        laboratory_id = 1
        
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        firstname = 'Jean-Christophe'
        lastname = 'Orain'
        status_id = 2
        laboratory_id = 3
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
        
        firstname = 'Gediminas'
        lastname = 'Simutis'
        status_id = 2
        laboratory_id = 3
        tables_update.add_row_user_table(firstname, lastname, status_id, laboratory_id, connection)
       
        laboratory_name = database_utils.fetchall_query(connection, 'SELECT name FROM laboratory WHERE id = {}'.format(laboratory_id))[0][0] 
       
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM user')
        
        assert 'The user table has been created.' in captured.out
        assert 'The user {} {} ({}) has been succesfully added to the database.'.format(firstname, lastname, laboratory_name) in captured.out
        assert existing_values == [(1,
                                    'Jean-Christophe',
                                    'Orain',
                                    1,
                                    1),
                                   (2,
                                    'Jean-Christophe',
                                    'Orain',
                                    2,
                                    3),
                                   (3,
                                    'Gediminas',
                                    'Simutis',
                                    2,
                                    3)]
    
class TestAdd_row_experiment_setup_table():
    '''
    Class to test the add row function for the experiment_setup table 
    '''
    def test_add_row_experiment_setup_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        connection = None
        
        res = tables_update.add_row_experiment_setup_table(name, 
                                                           roomname,
                                                           experimental_setup_start_date, 
                                                           min_field, 
                                                           max_field, 
                                                           min_temperature,
                                                           max_temperature,
                                                           experiment_type_id, 
                                                           responsible_id,
                                                           connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None

    def test_add_row_experiment_setup_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        
        res = tables_update.add_row_experiment_setup_table(name, 
                                                           roomname,
                                                           experimental_setup_start_date, 
                                                           min_field, 
                                                           max_field, 
                                                           min_temperature,
                                                           max_temperature,
                                                           experiment_type_id, 
                                                           responsible_id,
                                                           connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no experiment setup name. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_experiment_setup_no_roomname(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no room name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'MMPS He4'
        roomname = None
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        
        res = tables_update.add_row_experiment_setup_table(name, 
                                                           roomname,
                                                           experimental_setup_start_date, 
                                                           min_field, 
                                                           max_field, 
                                                           min_temperature,
                                                           max_temperature,
                                                           experiment_type_id, 
                                                           responsible_id,
                                                           connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no experiment setup room name. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_experiment_setup_no_startdate(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no start date 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = None
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        
        res = tables_update.add_row_experiment_setup_table(name, 
                                                           roomname,
                                                           experimental_setup_start_date, 
                                                           min_field, 
                                                           max_field, 
                                                           min_temperature,
                                                           max_temperature,
                                                           experiment_type_id, 
                                                           responsible_id,
                                                           connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no experiment setup start date. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_experiment_setup_no_experiment_type_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no experiement_type id 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = None
        responsible_id = 1
        
        res = tables_update.add_row_experiment_setup_table(name, 
                                                           roomname,
                                                           experimental_setup_start_date, 
                                                           min_field, 
                                                           max_field, 
                                                           min_temperature,
                                                           max_temperature,
                                                           experiment_type_id, 
                                                           responsible_id,
                                                           connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no experiment_type_id for the experiment setup. Please provide it' in captured.out
        
        assert res == None
        
        
    def test_add_row_experiment_setup_no_responsible_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no responsible id
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = None
        
        res = tables_update.add_row_experiment_setup_table(name, 
                                                           roomname,
                                                           experimental_setup_start_date, 
                                                           min_field, 
                                                           max_field, 
                                                           min_temperature,
                                                           max_temperature,
                                                           experiment_type_id, 
                                                           responsible_id,
                                                           connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no responsible_id for the experiment setup. Please provide it' in captured.out
        
        assert res == None


    def test_add_row_experiment_setup_no_user_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no status table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
         
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_setup')
        
        assert "The error 'no such table: main.user' occurred" in captured.out
        assert existing_values == []    
        
    def test_add_row_experiment_setup_no_experiment_type_table(self, capsys, create_example_db_user):
        '''
        function to test the behavior of the function when there is no experiment type table 
        '''
        
        connection = create_example_db_user
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
         
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_setup')
        
        assert "The error 'no such table: main.experiment_type' occurred" in captured.out
        assert existing_values == []
        
    def test_add_row_experiment_setup_new_table(self, capsys, create_example_db_user_experiment_type):
        '''
        function to test the behavior of the function when there is new table
        '''
        
        connection = create_example_db_user_experiment_type
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
         
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_setup')
        
        assert 'The experiment_setup table has been created.' in captured.out
        assert 'The experiment setup {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'MMPS He4',
                                    'Salon',
                                    '25/05/2018',
                                    0,
                                    5,
                                    1.5,
                                    300,
                                    1,
                                    1)]
        
    def test_add_row_experiment_setup_same_values(self, capsys, create_example_db_user_experiment_type):
        '''
        function to test the behavior of the function when there the same values
        '''
        
        connection = create_example_db_user_experiment_type
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
        
        name = 'MMPS He4'
        roomname = 'SalonBis'
        experimental_setup_start_date = '25/05/2018Test'
        min_field = 10
        max_field = 25
        min_temperature = 1
        max_temperature = 3000
        experiment_type_id = 2
        responsible_id = 1
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
        
        responsible_name = database_utils.fetchall_query(connection, 'SELECT firstname, lastname FROM user WHERE id = {};'.format(responsible_id))[0]
       
        captured = capsys.readouterr()
        
        assert 'The experiment setup {} under the responsibility of {} {} already exists and will not be added to the database.'.format(name, responsible_name[0], responsible_name[1]) in captured.out

    def test_add_row_experiment_setup_wrong_responsible_id(self, capsys, create_example_db_user_experiment_type):
        '''
        function to test the behavior of the function when there is a wrong responsible id
        '''
        
        connection = create_example_db_user_experiment_type
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 5
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
         
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_setup')
        
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []

    def test_add_row_experiment_setup_wrong_eyperiment_type_id(self, capsys, create_example_db_user_experiment_type):
        '''
        function to test the behavior of the function when there is a wrong experiment_type id
        '''
        
        connection = create_example_db_user_experiment_type
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 5
        responsible_id = 1
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
         
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_setup')
        
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []

    def test_add_row_experiment_setup_two_rows(self, capsys, create_example_db_user_experiment_type):
        '''
        function to test the behavior of the function when setting two rows 
        '''
        
        connection = create_example_db_user_experiment_type
        
        name = 'MMPS He4'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = 0
        max_field = 5
        min_temperature = 1.5
        max_temperature = 300
        experiment_type_id = 1
        responsible_id = 1
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
        
        name = 'MMPS He4 bis'
        roomname = 'Salon'
        experimental_setup_start_date = '25/05/2018'
        min_field = None
        max_field = None
        min_temperature = None
        max_temperature = None
        experiment_type_id = 1
        responsible_id = 2
        
        tables_update.add_row_experiment_setup_table(name, 
                                                     roomname,
                                                     experimental_setup_start_date, 
                                                     min_field, 
                                                     max_field, 
                                                     min_temperature,
                                                     max_temperature,
                                                     experiment_type_id, 
                                                     responsible_id,
                                                     connection)
        
         
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM experiment_setup')
        
        assert 'The experiment_setup table has been created.' in captured.out
        assert 'The experiment setup {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    'MMPS He4',
                                    'Salon',
                                    '25/05/2018',
                                    0,
                                    5,
                                    1.5,
                                    300,
                                    1,
                                    1),
                                   (2,
                                    'MMPS He4 bis',
                                    'Salon',
                                    '25/05/2018',
                                    None,
                                    None,
                                    None,
                                    None,
                                    1,
                                    2)]

class TestAdd_row_batch_table():
     '''
     Class to test the add row function for the batch table 
     '''
     def test_add_row_batch_no_connection(self, capsys):
       '''
       function to test the behavior of the function when there is no connection 
       '''
       name = "DQVOF 1"
       mass = 100
       color = 'green'
       Type = "powder"
       creation_date = '2019-10-12'
       compound_id = 1
       grower_id = 1
       connection = None
      
       res = tables_update.add_row_batch_table(name,
                                               mass,
                                               color,
                                               Type,
                                               creation_date,
                                               compound_id,
                                               grower_id,
                                               connection)
      
       captured = capsys.readouterr()
      
       assert 'There is no connection to an SQL database. Please initiate it' in captured.out
      
       assert res == None
         
     def test_add_row_batch_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        #  create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        res = tables_update.add_row_batch_table(name,
                                                mass,
                                                color,
                                                Type,
                                                creation_date,
                                                compound_id,
                                                grower_id,
                                                connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no batch name. Please provide it' in captured.out
        
        assert res == None
        
     def test_add_row_batch_no_mass(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no mass 
        '''
        #  create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "DQVOF 1"
        mass = None
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        res = tables_update.add_row_batch_table(name,
                                                mass,
                                                color,
                                                Type,
                                                creation_date,
                                                compound_id,
                                                grower_id,
                                                connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no batch mass. Please provide it' in captured.out
        
        assert res == None
        
     def test_add_row_batch_no_color(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no color 
        '''
        #  create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "DQVOF 1"
        mass = 100
        color = None
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        res = tables_update.add_row_batch_table(name,
                                                mass,
                                                color,
                                                Type,
                                                creation_date,
                                                compound_id,
                                                grower_id,
                                                connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no batch color. Please provide it' in captured.out
        
        assert res == None
        
     def test_add_row_batch_no_type(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no type
        '''
        #  create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = None
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        res = tables_update.add_row_batch_table(name,
                                                mass,
                                                color,
                                                Type,
                                                creation_date,
                                                compound_id,
                                                grower_id,
                                                connection)
        
        captured = capsys.readouterr()
        
        assert 'The batch type is not in the list "powder", "polycristal" or "single cristal". Please make a choice' in captured.out
        
        assert res == None
        
     def test_add_row_batch_no_creation_date(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no creation date 
        '''
        #  create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = None
        compound_id = 1
        grower_id = 1
        
        res = tables_update.add_row_batch_table(name,
                                                mass,
                                                color,
                                                Type,
                                                creation_date,
                                                compound_id,
                                                grower_id,
                                                connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no batch creation date. Please provide it' in captured.out
        
        assert res == None
        
     def test_add_row_batch_no_compound_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no compound_id
        '''
        #  create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = None
        grower_id = 1
        
        res = tables_update.add_row_batch_table(name,
                                                mass,
                                                color,
                                                Type,
                                                creation_date,
                                                compound_id,
                                                grower_id,
                                                connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no compound_id for the batch. Please provide it' in captured.out
        
        assert res == None
        
     def test_add_row_batch_no_grower_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no mass 
        '''
        #  create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = None
        
        res = tables_update.add_row_batch_table(name,
                                                mass,
                                                color,
                                                Type,
                                                creation_date,
                                                compound_id,
                                                grower_id,
                                                connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no grower_id for the batch. Please provide it' in captured.out
        
        assert res == None
        
     def test_add_row_batch_no_user_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no user table
        '''
        #  create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM batch')
            
        assert "The error 'no such table: main.user' occurred" in captured.out
        assert existing_values == []    

     def test_add_row_batch_no_compound_table(self, capsys, create_example_db_user):
        '''
        function to test the behavior of the function when there is no user table
        '''
        #  create an empty connection with foreign keys ON
        connection = create_example_db_user
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM batch')
            
        assert "The error 'no such table: main.compound' occurred" in captured.out
        assert existing_values == []  

     def test_add_row_batch_no_compound_new_table(self, capsys, create_example_db_user_compound):
        '''
        function to test the behavior of the function when creating a new table
        '''
        #  create an empty connection with foreign keys ON
        connection = create_example_db_user_compound
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM batch')

        assert 'The batch table has been created.' in captured.out
        assert 'The batch {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    "DQVOF 1",
                                    100,
                                    'green',
                                    "powder",
                                    '2019-10-12',
                                    1,
                                    1)]
         
     def test_add_row_batch_no_compound_same_values(self, capsys, create_example_db_user_compound):
        '''
        function to test the behavior of the function when adding the same values
        '''
        #  create an empty connection with foreign keys ON
        connection = create_example_db_user_compound
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        name = "DQVOF 1"
        mass = 1200
        color = 'green bis'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        captured = capsys.readouterr()
        
        assert 'The batch {} already exists and will not be added to the database.'.format(name) in captured.out

     def test_add_row_batch_no_compound_wrong_grower_id(self, capsys, create_example_db_user_compound):
        '''
        function to test the behavior of the function when setting unknown grower
        '''
        #  create an empty connection with foreign keys ON
        connection = create_example_db_user_compound
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 5
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM batch')
        
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []

     def test_add_row_batch_no_compound_wrong_compound_id(self, capsys, create_example_db_user_compound):
        '''
        function to test the behavior of the function when setting unknown compound
        '''
        #  create an empty connection with foreign keys ON
        connection = create_example_db_user_compound
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 5
        grower_id = 1
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM batch')
        
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []

     def test_add_row_batch_no_compound_wrong_batch_type(self, capsys, create_example_db_user_compound):
        '''
        function to test the behavior of the function when setting wrong type
        '''
        #  create an empty connection with foreign keys ON
        connection = create_example_db_user_compound
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "test"
        creation_date = '2019-10-12'
        compound_id = 2
        grower_id = 1
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        captured = capsys.readouterr()
                
        assert 'The batch type is not in the list "powder", "polycristal" or "single cristal". Please make a choice' in captured.out

     def test_add_row_batch_no_compound_two_rows(self, capsys, create_example_db_user_compound):
        '''
        function to test the behavior of the function when adding two rows
        '''
        #  create an empty connection with foreign keys ON
        connection = create_example_db_user_compound
        
        name = "DQVOF 1"
        mass = 100
        color = 'green'
        Type = "powder"
        creation_date = '2019-10-12'
        compound_id = 1
        grower_id = 1
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        name = "Test 2002"
        mass = 200
        color = 'green'
        Type = "single cristal"
        creation_date = '2017-10-12'
        compound_id = 2
        grower_id = 3
        
        tables_update.add_row_batch_table(name,
                                          mass,
                                          color,
                                          Type,
                                          creation_date,
                                          compound_id,
                                          grower_id,
                                          connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM batch')
        
        assert 'The batch table has been created.' in captured.out
        assert 'The batch {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    "DQVOF 1",
                                    100,
                                    'green',
                                    "powder",
                                    '2019-10-12',
                                    1,
                                    1),
                                   (2,
                                    "Test 2002",
                                    200,
                                    'green',
                                    "single cristal",
                                    '2017-10-12',
                                    2,
                                    3)] 
        
class TestAdd_row_project_table():
    '''
    Class to test the add row function for the project table 
    '''
    def test_add_row_project_no_connection(self, capsys):
        '''
        function to test the behavior of the function when there is no connection 
        '''
        name = "Super project"
        project_responsible_id = 1
        connection = None
        
        res = tables_update.add_row_project_table(name, 
                                                  project_responsible_id, 
                                                  connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
        assert res == None
        
    def test_add_row_project_no_name(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no name 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = None
        project_responsible_id = 1
        
        res = tables_update.add_row_project_table(name, 
                                                  project_responsible_id, 
                                                  connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no project name. Please provide it' in captured.out
        
        assert res == None
    
    def test_add_row_project_no_project_responsible_id(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no responsible_id 
        '''
        # create an empty connection with foreign keys ON
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "Super project"
        project_responsible_id = None
        
        res = tables_update.add_row_project_table(name, 
                                                  project_responsible_id, 
                                                  connection)
        
        captured = capsys.readouterr()
        
        assert 'There is no responsible_id for the experiment setup. Please provide it' in captured.out
        
        assert res == None
        
    def test_add_row_project_no_user_table(self, capsys, tmp_path):
        '''
        function to test the behavior of the function when there is no user table 
        '''
        
        name_db = 'database_test.sqlite'
        connection = database_utils.create_or_connect_db(tmp_path, name_db)
        
        name = "Super project"
        project_responsible_id = 1
        
        tables_update.add_row_project_table(name, 
                                                  project_responsible_id, 
                                                  connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM project')
        
        assert "The error 'no such table: main.user' occurred" in captured.out
        assert existing_values == []

    def test_add_row_project_new_table(self, capsys, create_example_db_user):
        '''
        function to test the behavior of the function when adding new table
        '''
        
        connection =  create_example_db_user
        
        name = "Super project"
        project_responsible_id = 1
        
        tables_update.add_row_project_table(name, 
                                                  project_responsible_id, 
                                                  connection)
        
        captured = capsys.readouterr()
        
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM project')
        
        assert 'The project table has been created.' in captured.out
        assert 'The project {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    "Super project", 
                                    1)]

    def test_add_row_project_same_values(self, capsys, create_example_db_user):
        '''
        function to test the behavior of the function when getting same laboratory name
        '''
        
        connection =  create_example_db_user
        
        name = "Super project"
        project_responsible_id = 1
        
        tables_update.add_row_project_table(name, 
                                            project_responsible_id, 
                                            connection)
        
        # recretae the same data 
        
        project_responsible_id = 2
        
        tables_update.add_row_project_table(name, 
                                            project_responsible_id, 
                                            connection)
        
        captured = capsys.readouterr()
                
        
        assert 'The project {} already exists and will not be added to the database.'.format(name) in captured.out

    def test_add_row_laboratory_wrong_responsible_id(self, capsys, create_example_db_user):
        '''
        function to test the behavior of the function when having unknown responsible id number 
        '''
        
        connection =  create_example_db_user
        
        name = "Super project"
        project_responsible_id = 5
        
        tables_update.add_row_project_table(name, 
                                            project_responsible_id, 
                                            connection)
        
        captured = capsys.readouterr()
          
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM project')
                
        assert "The error 'FOREIGN KEY constraint failed' occurred" in captured.out
        assert existing_values == []

    def test_add_row_project_two_rows(self, capsys, create_example_db_user):
        '''
        function to test the behavior of the function with different rows
        '''
        
        connection =  create_example_db_user
        
        name = "Super project"
        project_responsible_id = 1
        
        tables_update.add_row_project_table(name, 
                                            project_responsible_id, 
                                            connection)
        
        name = "Super other project"
        project_responsible_id = 3
        
        tables_update.add_row_project_table(name, 
                                            project_responsible_id, 
                                            connection)
             
        captured = capsys.readouterr()
                
        existing_values = database_utils.fetchall_query(connection, 'SELECT * FROM project')
        
        assert 'The project table has been created.' in captured.out
        assert 'The project {} has been succesfully added to the database.'.format(name) in captured.out
        assert existing_values == [(1,
                                    "Super project", 
                                    1),
                                   (2,
                                    "Super other project", 
                                    3)]