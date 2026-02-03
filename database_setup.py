import sqlite3


def init_db():
    conn = sqlite3.connect('reltix_ops.db')
    cursor = conn.cursor()

    # Creating a table for Properties
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY,
            address TEXT,
            owner_name TEXT,
            tenant_email TEXT
        )
    ''')

    # Creating a table for Maintenance Tickets
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_id INTEGER,
            issue_description TEXT,
            urgency_score INTEGER,
            status TEXT,
            FOREIGN KEY (property_id) REFERENCES properties (id)
        )
    ''')


    cursor.execute(
        "INSERT OR IGNORE INTO properties VALUES (1, 'Main St 10, Berlin', 'Max Mustermann', 'tenant1@example.com')")
    cursor.execute(
        "INSERT OR IGNORE INTO properties VALUES (2, 'Bahnstrasse 5, Munich', 'Julia Schmidt', 'tenant2@example.com')")

    conn.commit()
    conn.close()
    print("Database initialized: reltix_ops.db")


if __name__ == "__main__":
    init_db()