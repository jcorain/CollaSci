'''
test module for the database_utils module
'''
import pytest
import os 
import shutil
import CollaSci.db_function.database_utils as database_utils

class Testcreate_or_connect_db():
    '''
    Class to test create_or_connect_db function 
    '''
    def test_create_or_connect_db_no_path(self):
        '''
        Function to test if None path returns an error

        Returns
        -------
        None.

        '''
        path = None
        with pytest.raises(TypeError) as error:
            database_utils.create_or_connect_db(path = path)
        assert "expected str, bytes or os.PathLike object, not NoneType" in str(error)
            
    def test_create_or_connect_db_no_name(self):
        '''
        Function to test if None name returns an error

        Returns
        -------
        None.

        '''
        name = None
        with pytest.raises(TypeError) as error:
            database_utils.create_or_connect_db(name = name)
        assert "join() argument must be str, bytes, or os.PathLike object, not 'NoneType'" in str(error)
            
    def test_create_or_connect_db_create(self, tmp_path):
        '''
        Function to check if we can create a database

        Parameters
        ----------
        tmp_path : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        connection = database_utils.create_or_connect_db(path = tmp_path)
        connection.close()
        assert 'sqlite3.Connection object' in str(connection)
        
    def test_create_or_connect_db_connect(self, example_connection_path_name):
        '''
        Function to check if we can connect to an existing database

        Parameters
        ----------
        tmp_path : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        path, name = example_connection_path_name
        connection = database_utils.create_or_connect_db(path = path, name = name)
        connection.close()
        assert 'sqlite3.Connection object' in str(connection)
        
class TestExecute_query():
    '''
    Class to test the execute query function
    '''
    def test_execute_querry_no_connection(self):
        '''
        Function to test the execution when no connection is provided

        Returns
        -------
        None.

        '''
        connection = None
        query = ''
        with pytest.raises(AttributeError) as error:
            database_utils.execute_query(connection = connection, query = query)
        assert "'NoneType' object has no attribute 'cursor'" in str(error)
        
        
    def test_execute_querry_no_query(self, create_example_db):
        '''
        Function to test the execution when no query is provided

        Returns
        -------
        None.

        '''
        connection = create_example_db
        query = None
        with pytest.raises(TypeError) as error:
            database_utils.execute_query(connection = connection, query = query)
        
        connection.close()
        
        assert "argument 1 must be str, not None" in str(error)
        
    def test_execute_querry_wrong_query(self, create_example_db, capsys):
        '''
        Function to test the execution when wrong query is provided

        Returns
        -------
        None.

        '''
        connection = create_example_db
        query = 'SELECT * FROM test'
        ret = database_utils.execute_query(connection = connection, query = query)
        
            
        captured = capsys.readouterr()
        
        connection.close()        
        assert "The error 'no such table: test' occurred" in captured.out
        assert ret == False
        
    def test_execute_querry(self, create_example_db, capsys):
        '''
        Function to test the good execution without values

        Returns
        -------
        None.

        '''
        connection = create_example_db
        query = 'SELECT * FROM user'
        ret = database_utils.execute_query(connection = connection, query = query)
        connection.close()
        captured = capsys.readouterr()
        assert captured.out == "Query executed successfully\n"
        assert ret == True
        
    def test_execute_querry_wrong_values(self, create_example_db, capsys):
        '''
        Function to test the execution when wrong values is provided

        Returns
        -------
        None.

        '''
        connection = create_example_db
        query = 'SELECT * FROM user'
        ret = database_utils.execute_query(connection = connection, query = query, values = (1,))
        connection.close()
        
        captured = capsys.readouterr()
        
        assert captured.out == "The error 'Incorrect number of bindings supplied. The current statement uses 0, and there are 1 supplied.' occurred\n"
        assert ret == False

    def test_execute_querry_good_values(self, create_example_db, capsys):
        '''
        Function to test the execution with values

        Returns
        -------
        None.

        '''
        connection = create_example_db
        query = """
        INSERT INTO 
            university(name, country, city, address)
        VALUES
            (?, ?, ?, ?)
        """
        ret = database_utils.execute_query(connection = connection, query = query, values = ('test','test','test','test'))
        
        
        captured = capsys.readouterr()
        # delete the  last row
        
        database_utils.delete_id_from_table(connection, 'university', 3)
        
        connection.close()
        assert captured.out == "Query executed successfully\n"
        assert ret == True
        
        

class TestFetchall_query():
    '''
    Class to test the fetchall query function
    '''
    def test_fetchall_querry_no_connection(self):
        '''
        Function to test the fetchall when no connection is provided

        Returns
        -------
        None.

        '''
        connection = None
        query = ''
        with pytest.raises(AttributeError) as error:
            database_utils.fetchall_query(connection = connection, query = query)
        assert "'NoneType' object has no attribute 'cursor'" in str(error)
        
        
    def test_fetchall_querry_no_query(self, create_example_db):
        '''
        Function to test the fetchall when no query is provided

        Returns
        -------
        None.

        '''
        connection = create_example_db
        query = None
        with pytest.raises(TypeError) as error:
            database_utils.fetchall_query(connection = connection, query = query)
        connection.close()
        assert "argument 1 must be str, not None" in str(error)
        
    def test_fetchall_querry_wrong_query(self, create_example_db, capsys):
        '''
        Function to test the fetchall when wrong querry is provided

        Returns
        -------
        None.

        '''
        connection = create_example_db
        query = 'SELECT * FROM test'
        ret = database_utils.fetchall_query(connection = connection, query = query)
        
        captured = capsys.readouterr()
        
        connection.close()
        
        assert captured.out == "The error 'no such table: test' occurred\n"
        assert ret == None
        
    def test_fetchall_querry(self, create_example_db, capsys):
        '''
        Function to test the good fetchall

        Returns
        -------
        None.

        '''
        connection = create_example_db
        query = 'SELECT * FROM user'
        ret = database_utils.fetchall_query(connection = connection, query = query)
        
        captured = capsys.readouterr()
        
        connection.close()
        
        assert captured.out == "Query fetched successfully\n"
        assert ret ==  [(1, 'Jean-Christophe', 'Orain', 1, 1),
                        (2, 'Jean-Christophe', 'Orain', 2, 3), 
                        (3, 'Gediminas', 'Simutis', 2, 3)]
    
class TestCheck_table_exists():
    def test_check_tabl_exists_no_connection(self):
        '''
        Function to check table_exists function when there is no connection 

        Returns
        -------
        None.

        '''
        connection = None
        table_name = 'test'
        with pytest.raises(AttributeError) as error:
            database_utils.check_table_exists(connection = connection, table_name = table_name)
        assert "'NoneType' object has no attribute 'cursor'" in str(error)
    
    def test_check_tabl_exists_no_table_name(self,create_example_db, capsys):
        '''
        Function to check table_exists function when there is no connection 

        Returns
        -------
        None.

        '''
        connection = create_example_db
        table_name = None
        
        ret = database_utils.check_table_exists(connection = connection, table_name = table_name)
        captured = capsys.readouterr()
        
        connection.close()
        
        assert captured.out == 'There is no table name. Please provide it.\n'
        assert ret == None

    def test_check_tabl_exists_wrong_table_name(self,create_example_db):
        '''
        Function to check table_exists function when there is no connection 

        Returns
        -------
        None.

        '''
        connection = create_example_db
        table_name = 'test'
        
        ret = database_utils.check_table_exists(connection = connection, table_name = table_name)
        
        connection.close()
        
        assert ret == False

    def test_check_tabl_exists(self,create_example_db):
        '''
        Function to check table_exists function when there is no connection 

        Returns
        -------
        None.

        '''
        connection = create_example_db
        table_name = 'user'
        
        ret = database_utils.check_table_exists(connection = connection, table_name = table_name)
        
        connection.close()
        assert ret == True

class TestDelete_id_from_table():
    '''
    Test class to check the delete_id_from_table function
    '''
    def test_delete_id_from_table_no_connection(self):
        connection = None
        table_name = 'test'
        id_num = 1
        with pytest.raises(AttributeError) as error:
            database_utils.delete_id_from_table(connection = connection, table_name = table_name, id_num = id_num)
        assert "'NoneType' object has no attribute 'cursor'" in str(error)
        
    def test_delete_id_from_table_no_table_name(self, create_example_db, capsys):
        connection = create_example_db
        table_name = None
        id_num = 1
        database_utils.delete_id_from_table(connection = connection, table_name = table_name, id_num = id_num)
        captured = capsys.readouterr()
        
        connection.close()
        
        assert captured.out == "The error 'no such table: None' occurred\n"

    def test_delete_id_from_table_wrong_table_name(self, create_example_db, capsys):
        connection = create_example_db
        table_name = 'test'
        id_num = 1
        database_utils.delete_id_from_table(connection = connection, table_name = table_name, id_num = id_num)
        captured = capsys.readouterr()
       
        connection.close()
        
        assert captured.out == "The error 'no such table: test' occurred\n"
        
    def test_delete_id_from_table_no_id_num(self, create_example_db, capsys):
        connection = create_example_db
        table_name = 'university'
        id_num = None
        database_utils.delete_id_from_table(connection = connection, table_name = table_name, id_num = id_num)
        captured = capsys.readouterr()
        universities = database_utils.fetchall_query(connection, "SELECT name FROM university;")
        connection.close()
       
        assert "The row number None has been successfully deleted from the university table" in captured.out
        assert sorted(universities) == sorted([('Université Paris Saclay',), 
                                              ('Paul Scherrer Institute',)])
    def test_delete_id_from_table_wrong_id_num(self, create_example_db, capsys):
        connection = create_example_db
        table_name = 'university'
        id_num = 10
        database_utils.delete_id_from_table(connection = connection, table_name = table_name, id_num = id_num)
        
        captured = capsys.readouterr()
        
        universities = database_utils.fetchall_query(connection, "SELECT name FROM university;")
        user = database_utils.fetchall_query(connection, "SELECT firstname FROM user;")
        
        connection.close()
                      
        assert "The row number 10 has been successfully deleted from the university table" in captured.out
        assert sorted(universities) == sorted([('Université Paris Saclay',), 
                                                ('Paul Scherrer Institute',)])
        assert user == [('Jean-Christophe',), 
                        ('Jean-Christophe',), 
                        ('Gediminas',)]

    def test_delete_id_from_table(self, create_example_db, capsys):
        connection = create_example_db
        table_name = 'university'
        id_num = 1
        database_utils.delete_id_from_table(connection = connection, table_name = table_name, id_num = id_num)
        
        captured = capsys.readouterr()
        
        
        # check the users and universities names 
        universities = database_utils.fetchall_query(connection, "SELECT name FROM university;")
        user = database_utils.fetchall_query(connection, "SELECT lastname FROM user;")
        connection.close()
        
        assert "The row number 1 has been successfully deleted from the university table" in captured.out
        assert universities == [('Paul Scherrer Institute',)]
        assert user == [('Orain',),('Simutis',)]
        
        
        
