# sample_query.py

import sqlite3
import time

db_conn = sqlite3.connect("people_db.db")
db_cursor = db_conn.cursor()

t1 = time.perf_counter_ns()

db_cursor.execute("SELECT name, email FROM people WHERE job='Product manager' LIMIT 10;")

res = db_cursor.fetchall()
t2 = time.perf_counter_ns()

print(res)
print(f"Query time without index: {(t2-t1)/1000} us") # update this line when re-running after creating index
