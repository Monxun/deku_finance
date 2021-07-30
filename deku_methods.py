from iexfinance.stocks import Stock # UPDATE TO IMPORT WHOLE LIBRARY
from psycopg2 import connect
import pandas
import datetime
import config

#_________________________'DATABASE'____________________________
#
# PASS THE SYMBOL, TABLE, and SQL QUERY TO THE DB_UPDATE METHOD
#
#*WORKS* NEEDS TESTING
def DB_UPDATE(table='stock'):

    table_name = table

    # declare connection instance
    conn = connect(
        dbname = config.DB_NAME,
        user = config.DB_USER,
        host = 'host.docker.internal',
        password = config.DB_PASSWORD
    )

    # declare a cursor object from the connection
    cursor = conn.cursor()

    # execute an SQL statement using the psycopg2 cursor object
    cursor.execute(f"SELECT * FROM {table_name};")

    # enumerate() over the PostgreSQL records
    for i, record in enumerate(cursor):
        print ("\n", type(record))
        print ( record )

    # close the cursor object to avoid memory leaks
    cursor.close()

    # close the connection as well
    conn.close()

# DB_UPDATE()


#_____________________________'API'______________________________
#
# DESIGNED TO GRAB STOCKS FROM IEX. NEEDS TO BE MODIFIED FOR CUSTOMIZATION OF ARGS
# *WORKS* NEEDS TESTINGn | SYMBOLS WILL HAVE ATTRIBUTE DATA INCLUDING ITS TYPE 
# (CRYPT, STOCK, FOREX, ETC... UNDER 'INST_TYPE')

def get_symbol_data(symbol, type, info):

    start = datetime.date(2020, 7, 1) # create attribute to pass range of data

    if type == 'stock':
        stock = Stock(symbol, token=config.api_key)
    if info =='get_company':
        a = stock.get_company()

    print(a)

#_____________________________'MATH'______________________________
#
# The idea here is to write methods to: 
# 1: normalize ohlcv/ticker/sentiment series data using diferencing method - DONE
# 2: run method that performs spearmans rank correlation coefficient on returned list
# 3: write list to corresponding 'correlation' table columns using timestamp as index
# 4:

# *WORKS* NEEDS TESTING
def differencing(a: list, b: list) -> list:

    # list_a = []
    # list_b = []
    list_result = []

    for item in a:
        index = b.index(item)
        result = a[index] - b[index]
        list_result.append(result)
        
    return list_result


get_symbol_data('TSLA', type='stock')