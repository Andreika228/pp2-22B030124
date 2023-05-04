import psycopg2 
 
conn = psycopg2.connect( 
    host="localhost", 
    database="postgres", 
    user="postgres", 
    password="retryfy1" 
) 
 
cur = conn.cursor() 
cur.execute("SELECT version();") 
print(cur.fetchone()) 
cur.close() 
conn.close()