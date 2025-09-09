# create_index.py

import time
import sqlite3

db_conn = sqlite3.connect('people_db.db')

db_cursor =db_conn.cursor()

t1 = time.perf_counter_ns()

db_cursor.execute("CREATE INDEX people_job_index ON people (job)")

t2 = time.perf_counter_ns()

db_conn.commit()

print(f"Time to create index: {(t2 - t1)/1000} us")
