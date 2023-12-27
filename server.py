import sqlite3
from fastapi import FastAPI
import uvicorn
from sqlite_helpers import *

DATABASE = 'url.db'
app = FastAPI()

create_table(DATABASE)


@app.get("/")
def root():
    return ({"message": "hello world"})


@app.get("/urls")
def get_all_urls():
    return list_all_urls(DATABASE)


@app.get("/url")
def alias_url(alias):
    return get_url_by_alias(alias, DATABASE)


@app.post('/insert')
def add_url(url, alias):
    return insert_url(url, alias, DATABASE)


@app.delete('/delete')
def add_url(alias):
    return delete_url(alias, DATABASE)


if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)
