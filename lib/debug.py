from __init__ import CONN, CURSOR
from department import Department

import ipdb


def reset_database():
    CURSOR.execute("DROP TABLE IF EXISTS departments")
    CURSOR.execute("""
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        )
    """)
    CONN.commit()

    Department.create("Payroll", "Building A, 5th Floor")
    Department.create("Human Resources", "Building C, East Wing")
    Department.create("Accounting", "Building B, 1st Floor")

reset_database()
ipdb.set_trace()