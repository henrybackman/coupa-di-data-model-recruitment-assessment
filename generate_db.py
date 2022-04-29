import sqlite3
con = sqlite3.connect('data.db')
cur = con.cursor()

cur.execute('''
DROP TABLE IF EXISTS orders;
''')
cur.execute('''
CREATE TABLE orders
    (
        order_no int,
        order_desc text,
        order_created_at date, 
        payment_term_code text, 
        order_status text
)
''')
cur.execute('''
DROP TABLE IF EXISTS order_lines;
''')
cur.execute('''
CREATE TABLE order_lines
    (
        order_line_no int,
        order_line_desc text,
        qty int, 
        order_line_delivered bool
)
''')
cur.execute('''
DROP TABLE IF EXISTS payment_terms;
''')
cur.execute('''
CREATE TABLE payment_terms
    (
        payment_term_code text,
        payment_term_desc text
)
''')

con.commit()
con.close()
