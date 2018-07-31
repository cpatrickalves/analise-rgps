#==============================================================================
#title           :csv_to_sqlite3.py
#description     :imports the data from CSV files and saves in a SQLite3 database
#author          :Patrick Alves
#date            :26-07-2018
#usage           :python csv_to_sqlite3.py
#python_version  :3.6
#encoding		 :utf-8
#==============================================================================

import sqlite3
import pandas as pd
import os

# Database files
db_file = 'microdadosRGPS.db'

# delete only if file exists 
if os.path.exists(db_file):
	os.remove(db_file)

# Creates database file and connect
conn = sqlite3.connect(db_file)
cursor = conn.cursor()  # This object lets us actually send messages to our DB and receive results

# chunks the CSV up and then load each chunk into the DB
counter = 0
chunksize = 10000

# First file: SEN_MICRODADOS01.APO.AUX.csv
apos_aux_file = '../microdados/CSV/SEN_MICRODADOS01.APO.AUX.csv'
for chunk in pd.read_csv(apos_aux_file, chunksize=chunksize, sep=';'):
	# Insert into table apos_aux
	chunk.to_sql(name='apos_aux', con=conn, if_exists='append', index=False)	
	
	counter += len(chunk)	
	print("\r" + "Copiando registros do arquivo {} - {}".format(apos_aux_file, str(counter)), end="")                                           
			
# Second file: SEN_MICRODADOS02_PENS.csv
print() # just print a blank line
counter = 0
pensoes_file = '../microdados/CSV/SEN_MICRODADOS02_PENS.csv'
for chunk in pd.read_csv(pensoes_file, chunksize=chunksize, sep=';'):
	# Insert into table pensoes
	chunk.to_sql(name='pensoes', con=conn, if_exists='append', index=False)
	counter += len(chunk)	
	print("\r" + "Copiando registros do arquivo {} - {}".format(pensoes_file, str(counter)), end="")                                           
	
conn.close()