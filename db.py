import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab",
    user="praptidhamala",
    password="your_password"
)

cur = conn.cursor()

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()