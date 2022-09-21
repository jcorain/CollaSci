import CollaSci.db_function.tables_create as tables_create
import CollaSci.db_function.database_utils as database_utils

class TestCreate_university_table():
    def test_create_university_table_no_connection(self, capsys):
        connection = None
        tables_create.create_university_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_university_table(self, capsys, tmp_path):
        connection = database_utils.create_or_connect_db(path = tmp_path)
        tables_create.create_university_table(connection)
        
        ret_uni = database_utils.check_table_exists(connection, 'university')
        ret_user = database_utils.check_table_exists(connection, 'user')
        connection.close()
        
        assert ret_uni == True
        assert ret_user == False
        
class TestCreate_laboratory_table():
    def test_create_laboratory_table_no_connection(self, capsys):
        connection = None
        tables_create.create_laboratory_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_laboratory_table(self, capsys, tmp_path):
        connection = database_utils.create_or_connect_db(path = tmp_path)
        tables_create.create_laboratory_table(connection)
        
        ret_uni = database_utils.check_table_exists(connection, 'laboratory')
        ret_user = database_utils.check_table_exists(connection, 'user')
        connection.close()
        
        assert ret_uni == True
        assert ret_user == False
        
class TestCreate_status_table():
    def test_create_status_table_no_connection(self, capsys):
        connection = None
        tables_create.create_status_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_status_table(self, capsys, tmp_path):
        connection = database_utils.create_or_connect_db(path = tmp_path)
        tables_create.create_status_table(connection)
        
        ret_uni = database_utils.check_table_exists(connection, 'status')
        ret_user = database_utils.check_table_exists(connection, 'user')
        connection.close()
        
        assert ret_uni == True
        assert ret_user == False

class TestCreate_material_type_table():
    def test_create_material_type_table_no_connection(self, capsys):
        connection = None
        tables_create.create_material_type_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_material_type_table(self, capsys, tmp_path):
        connection = database_utils.create_or_connect_db(path = tmp_path)
        tables_create.create_material_type_table(connection)
        
        ret_uni = database_utils.check_table_exists(connection, 'material_type')
        ret_user = database_utils.check_table_exists(connection, 'user')
        connection.close()
        
        assert ret_uni == True
        assert ret_user == False
        
class TestCreate_compound_table():
    def test_create_compound_table_no_connection(self, capsys):
        connection = None
        tables_create.create_compound_table(connection)
        captured = capsys.readouterr()
        
        assert 'There is no connection to an SQL database. Please initiate it' in captured.out
        
    def test_create_compound_table(self, capsys, tmp_path):
        connection = database_utils.create_or_connect_db(path = tmp_path)
        tables_create.create_compound_table(connection)
        
        ret_uni = database_utils.check_table_exists(connection, 'compound')
        ret_user = database_utils.check_table_exists(connection, 'material_type')
        
        uni = database_utils.fetchall_query(connection, "PRAGMA foreign_key_list(compound);")
        connection.close()
        print(uni)
        
        assert ret_uni == True
        assert ret_user == False
        assert 0 == 1