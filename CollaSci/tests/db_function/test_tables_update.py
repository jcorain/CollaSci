'''
test module for tables_update module
'''
import pytest

import CollaSci.db_function.tables_create as tables_create
import CollaSci.db_function.tables_update as tables_update
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
