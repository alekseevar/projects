
import psycopg2
import psycopg2.extras as extras
import pandas as pd


def execute_values(conn, df, table):
	tuples = [tuple(x) for x in df.to_numpy()]
	cols = ','.join(list(df.columns))
	# SQL query to execute
	query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
	cursor = conn.cursor()
	try:
		extras.execute_values(cursor, query, tuples)
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print("Error: %s" % error)
		conn.rollback()
		cursor.close()
		return 1
	print("execute_values() done")
	cursor.close()


# establishing connection
conn = psycopg2.connect(
	database="scraping_projects",
	user='ruslanaalekseeva',
	password='ruslanaalekseeva',
	host='127.0.0.1',
	port='5432'
)
sql = '''CREATE TABLE scraping_flats_project(id int , price char(20), 
address char(50) ,region char(60),rooms char(20),area char(40),floor char(20));'''

# creating a cursor
cursor = conn.cursor()
cursor.execute(sql)
data = pd.read_csv("flats_from_rieltor_ua.csv")

data = data[["price", "address", "region", "rooms", "area", "floor"]]

# using the function defined
execute_values(conn, data, 'scraping_flats_project')
