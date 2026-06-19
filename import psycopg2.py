import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab",
    user="praptidhamala",
    password="your_password"
)

cur = conn.cursor()

query = """
SELECT DISTINCT
    u.first_name,
    u.last_name,
    l.branch_name,
    l.city,
    l.district
FROM users u
LEFT JOIN transaction_tbl t
    ON u.user_id = t.user_id
LEFT JOIN location l
    ON t.location_id = l.location_id;
"""

cur.execute(query)

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()