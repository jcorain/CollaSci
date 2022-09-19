'''
test module for the database_utils module
'''
import pytest
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
            assert "join() argument must be str, bytes, or os.PathLike object, not 'NoneType'" in error
            
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
            assert "join() argument must be str, bytes, or os.PathLike object, not 'NoneType'" in error
            
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