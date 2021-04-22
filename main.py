from fastapi import FastAPI
from enum import Enum

app = FastAPI()


#Path parameters (with Enum)
#------------------------------
class Genres(str, Enum):
    rap = "rap"
    rock = "rock"
    metal = "metal"

@app.get("/genres/{genre}")
async def read_item(genre: Genres):
    if (genre == Genres.rap):
        return {"genre" : genre, "message" : "bruh"}
    if (genre == Genres.rock):
        return {"genre" : genre, "messsage" : "nice"}
    return {"genre" : genre, "message" : "nice"}
#------------------------------


#Query parameters
#------------------------------
fake_db_items = [{"name":"Foo"},{"name":"Bar"},{"name":"Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_db_items[skip : skip + limit]
#------------------------------