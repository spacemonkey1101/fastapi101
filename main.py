from fastapi import FastAPI, Path

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
# as soon as the function returns the dictionary is converted to a JSON
# this is a easier way for HTTP traffic to exchange
# fastapi handles JSONifying all of our data, so that we can work with python types
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


@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]


# multiple query params
@app.get("/get-item-brand/{item_id}/{name}")
def get_item_brand(item_id: int, name: str):
    return inventory[item_id]


# path function in FastAPI
# This allows to add more details, constraints to out path param
# if you dont pass a item_id we get None
@app.get("/get-item-path/{item_id}")
def get_item_path(item_id: int = Path(..., description="ID of the item you want to view",gt=0,le=1)):
    return inventory[item_id]

#query parameter
# we are going to take 1 query param called name
# by default if it does not get name in the URL path it will be a query param
@app.get("/get-by-name")
def get_by_name(name:str):
    for it in inventory:
        if inventory[it]["name"] == name:
            return inventory[it]
    return {'Data' : 'Not Found'}