import sqlite3
from fastapi import FastAPI, HTTPException
import uvicorn
from sqlite_helpers import *
from starlette.responses import RedirectResponse
from args import get_args


DATABASE = get_args().db
host = get_args().host
port = get_args().port
app = FastAPI()

create_table(DATABASE)


@app.get("/")
def root():
    return ({"message": "hello world"})


@app.get("/urls")
def get_all_urls():
    return list_all_urls(DATABASE)


@app.get("/url/{alias}")
def alias_url(alias):
    url_data = get_url_by_alias(alias, DATABASE)
    if url_data is not None:
        return RedirectResponse(url_data)
    elif url_data is None:
        raise HTTPException(status_code=404, detail="Alias not found")


@app.post('/insert')
def add_url(url, alias):
    return insert_url(url, alias, DATABASE)


@app.delete('/delete')
def add_url(alias):
    return delete_url(alias, DATABASE)


if __name__ == "__main__":
    uvicorn.run("server:app", host=host, port=port, reload=True)
