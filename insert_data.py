import sqlite3
import csv
con = sqlite3.connect('data.db')
cur = con.cursor()

# load data
rows = []
orders_collected = set()
payment_terms_collected = set()
order_inserts = []
payment_term_inserts = []
order_line_inserts = []
with open('data.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['order_no'] not in orders_collected:
            orders_collected.add(row['order_no'])
            order_inserts.append((
                row['order_no'],
                row['order_desc'],
                row['order_created_at'],
                row['payment_term_code'],
                row['order_status']
            ))

        order_line_inserts.append((
            row['order_line_no'],
            row['order_line_desc'],
            row['qty'],
            row['order_line_delivered']
        ))

        if row['payment_term_code'] not in payment_terms_collected:
            payment_terms_collected.add(row['payment_term_code'])
            payment_term_inserts.append((
                row['payment_term_code'],
                row['payment_term_desc']
            ))

# empty tables in case data already exists
cur.execute('DELETE FROM orders;')
cur.execute('DELETE FROM order_lines')
cur.execute('DELETE FROM payment_terms')

# insert data
cur.executemany('INSERT INTO orders VALUES (?,?,?,?,?)', order_inserts)
cur.executemany('INSERT INTO order_lines VALUES (?,?,?,?)',
                order_line_inserts)
cur.executemany('INSERT INTO payment_terms VALUES (?,?)',
                payment_term_inserts)

con.commit()
con.close()
