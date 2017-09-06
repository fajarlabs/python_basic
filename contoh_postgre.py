import psycopg2

try :
	conn = psycopg2.connect (
			user="postgres",
			password="postgres",
			host="127.0.0.1",
			database="pypg"
		)
	cur = conn.cursor()
	sql = '''
		  CREATE TABLE produk (
		  	  kode CHAR(4) NOT NULL PRIMARY KEY,
	 	      nama VARCHAR(25),
		   	  harga NUMERIC(9,2)
		  )
		  '''
	cur.execute(sql)
	conn.commit()
	cur.close()
	conn.close()
except psycopg2.OperationalError as e :
	print "Error : %s " % e