import sqlite3
from fastapi import FastAPI
import uvicorn
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()
connection_obj = sqlite3.connect('url.db')
cursor_obj = connection_obj.cursor()


# Creating table
table = """ CREATE TABLE IF NOT EXISTS URLTable (
            id INTEGER NOT NULL PRIMARY KEY,
            URL VARCHAR(255) NOT NULL,
            Alias VARCHAR(25) NOT NULL UNIQUE,
            timestamp TIMESTAMP
        ); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()


# insert url and their alias into the table
def insert_url(url, alias):
    conn = sqlite3.connect('url.db')
    cursor = conn.cursor()

    query = ''' INSERT INTO URLTable (URL, Alias, timestamp)
                VALUES (?, ?, ?) '''

    current_timestamp = datetime.now()

    cursor.execute(query, (url, alias, current_timestamp))

    conn.commit()

    conn.close()

# delete url given alias


def delete_url(alias):
    conn = sqlite3.connect('url.db')
    cursor = conn.cursor()

    query = ''' DELETE FROM URLTable WHERE Alias = ? '''

    cursor.execute(query, (alias,))

    conn.commit()

    conn.close()

# get all urls in the table


def list_all_urls():
    conn = sqlite3.connect('url.db')
    cursor = conn.cursor()

    query = ''' SELECT * FROM URLTable '''
    cursor.execute(query)

    urls = cursor.fetchall()

    # Close the connection
    conn.close()

    return urls

# get a specific url given the alias


def get_url_by_alias(alias):
    conn = sqlite3.connect('url.db')
    cursor = conn.cursor()

    query = ''' SELECT * FROM URLTable WHERE Alias = ? '''
    cursor.execute(query, (alias,))

    url_record = cursor.fetchone()

    conn.close()

    return url_record


print(list_all_urls())
