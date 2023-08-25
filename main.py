from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

# creates an API object
app = FastAPI()
"""
HTTP Request Methods
GET - endpoint that returns information
POST - sending/adding data to the enpoint
PUT - update data
DELETE - remove data
"""


# setting up root GET endpoint
@app.get("/")
def home():
    return {"Data": "Testing"}


# when we run our webserver and hit the root endpoint, it will return us the dictionary
# as soon as the function returns the dictionary is converted to a JSON object
# this is a easier way for HTTP traffic to exchange data
# fastapi handles JSONifying all of our data, so that we can work with python data types
# same happens we receive JSON data, fast api converts it to python types for us to work with


"""Running the webserver  
>uvicorn main:app --reload
>uvicorn <python filename>:<fastapi object> --reload
reload is to autoreload on change
"""


@app.get("/about")
def about():
    return {"Data": "About"}


# path parameter and query parameter
inventory = {
    1: {"name": "Milk", "price": 100, "brand": "Amul"},
    2: {"name": "Biscuits", "price": 200, "brand": "Parle"},
}

# endpoint that can retrieve for us the item info from inventory based on its id
""" var : type name == type hing == type annotation
This tells that the item_id should be an int
"""


# path parameter example
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]


# multiple path params
@app.get("/get-item-brand/{item_id}/{name}")
def get_item_brand(item_id: int, name: str):
    return inventory[item_id]


# path function in FastAPI
# This allows to add more details, constraints to our path param
# if you dont pass a item_id we get None
@app.get("/get-item-path/{item_id}")
def get_item_path(
    item_id: int = Path(..., description="ID of the item you want to view", gt=0, le=2)
):
    return inventory[item_id]


# query parameter
# we are going to take 1 query param called name
# by default if it does not get name in the URL path it will look for a query param called name
@app.get("/get-by-name")
def get_by_name(name: str):
    for it in inventory:
        if inventory[it]["name"] == name:
            return inventory[it]
    return {"Data": "Not Found"}


# add more details to query parameter and make them optional
# this will default to Data Not found when we do not pass a param


# this works but not recommended way
@app.get("/get-by-name-optional")
def get_by_name(name: str = None):
    for it in inventory:
        if inventory[it]["name"] == name:
            return inventory[it]
    return {"Data": "Not Found"}


# recommended way for optional pararm
@app.get("/get-by-name2")
def get_by_name(name: Optional[str] = None):
    for it in inventory:
        if inventory[it]["name"] == name:
            return inventory[it]
    return {"Data": "Not Found"}


# multiple query param
# defalut arg in python comes at last; to get around this use * at the start of the param list
@app.get("/get-by-name3")
def get_by_name(*, name: Optional[str] = None, test: str):
    for it in inventory:
        if inventory[it]["name"] == name:
            return inventory[it]
    return {"Data": "Not Found"}


# since test is a mandatory param we have to pass it
# the below query would work
# http://127.0.0.1:8000/get-by-name3?name=Milk&test=1
# http://127.0.0.1:8000/get-by-name3?test=1


# combine query and path params
# item_id is a path param, name is a optional query param, test is a mandatory query param
@app.get("/get-by-name4/{item_id}")
def get_by_name(*, item_id: int, name: Optional[str] = None, test: str):
    for it in inventory:
        if inventory[it]["name"] == name:
            return inventory[it]
    return {"Data": "Not Found"}


# this query works http://127.0.0.1:8000/get-by-name4/1?test=1&name=Milk
# also this http://127.0.0.1:8000/get-by-name4/1?test=q&name=Biscuits


# request body
class Item(BaseModel):
    """Item is defined in a way that access the kind of item our post method create_item would accept"""

    name: str
    price: float
    brand: Optional[str] = None


# post endpoint
# we will take some info from the request body and create an item in inventory
# we will define the Item type which inherits from BaseModel
# item is a class, fast api assumes that its not meant to be a query param
# instead its a request body
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item Id already exist"}
    inventory[item_id] = {"name": item.name, "price": item.price, "brand": item.brand}
    return inventory[item_id]
