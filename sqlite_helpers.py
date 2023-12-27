import sqlite3
from datetime import datetime

# Creating table


def create_table(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    table_query = """
    CREATE TABLE IF NOT EXISTS URLTable (
        id INTEGER NOT NULL PRIMARY KEY,
        URL VARCHAR(255) NOT NULL,
        Alias VARCHAR(25) NOT NULL UNIQUE,
        timestamp TIMESTAMP
    ); """

    cursor.execute(table_query)
    conn.commit()
    conn.close()


# insert url and their alias into the table
def insert_url(url, alias, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = ''' INSERT INTO URLTable (URL, Alias, timestamp)
                VALUES (?, ?, ?) '''

    current_timestamp = datetime.now()

    cursor.execute(query, (url, alias, current_timestamp))

    conn.commit()

    conn.close()

# delete url given alias


def delete_url(alias, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = ''' DELETE FROM URLTable WHERE Alias = ? '''

    cursor.execute(query, (alias,))

    conn.commit()

    conn.close()

# get all urls in the table


def list_all_urls(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = ''' SELECT * FROM URLTable '''
    cursor.execute(query)

    urls = cursor.fetchall()

    # Close the connection
    conn.close()

    return urls

# get a specific url given the alias


def get_url_by_alias(alias, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    query = ''' SELECT * FROM URLTable WHERE Alias = ? '''
    cursor.execute(query, (alias,))

    url_record = cursor.fetchone()

    conn.close()

    if url_record is not None:
        return url_record
    else:
        return None
