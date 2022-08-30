"""
module to update tables 
"""

import database_connect
import os
import sqlite3

def update_university_table(name, country, city, address):
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
    
    