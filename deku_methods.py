import pyEX as p
from psycopg2 import connect
import psycopg2.extras
import pandas
import datetime
import config

#_________________________'DATABASE'____________________________
#
# PASS THE SYMBOL, TABLE, and SQL QUERY TO THE DB_UPDATE METHOD
#
#


#*WORKS* NEEDS TESTING
def DB_POPULATE(symbol):


    # declare connection instance
    connection = connect(
        dbname = config.DB_NAME,
        user = config.DB_USER,
        host = 'host.docker.internal',
        password = config.DB_PASSWORD
    )

    # declare a cursor object from the connection
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

   

    # close the cursor object to avoid memory leaks
    cursor.close()

    # close the connection as well
    connection.close()

# DB_POPULATE()


#_____________________________'API'______________________________
#
# DESIGNED TO GRAB STOCKS FROM IEX. NEEDS TO BE MODIFIED FOR CUSTOMIZATION OF ARGS
# *WORKS* NEEDS TESTINGn | SYMBOLS WILL HAVE ATTRIBUTE DATA INCLUDING ITS TYPE 
# (CRYPT, STOCK, FOREX, ETC... UNDER 'INST_TYPE')


   

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
