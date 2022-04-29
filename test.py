import sqlite3
con = sqlite3.connect('data.db')
cur = con.cursor()

queries = [
    'orders',
    cur.execute('SELECT count(*) FROM orders').fetchone(),
    cur.execute('SELECT * FROM orders').fetchone(),
    cur.execute(
        'SELECT order_status, count(*) FROM orders GROUP BY 1').fetchall(),
    'order_lines',
    cur.execute('SELECT count(*) FROM order_lines').fetchone(),
    cur.execute('SELECT * FROM order_lines').fetchone(),
    'payment_terms',
    cur.execute('SELECT count(*) FROM payment_terms').fetchone(),
    cur.execute('SELECT * FROM payment_terms').fetchone()
]

for query in queries:
    print(query)
