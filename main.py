from fastapi import FastAPI

#creates an API object
app = FastAPI() 

'''
HTTP Request Methods
GET - endpoint that returns information
POST - sending/adding data to the enpoint
PUT - update data
DELETE - remove data
'''
#setting up root GET endpoint
@app.get("/")
def home():
    return {"Data":"Testing"}

# when we run our webserver and hit the root endpoint, it will return us the dictionary
# as soon as the function returns the dictionary is converted to a JSON
# this is a easier way for HTTP traffic to exchange
# fastapi handles JSONifying all of our data, so that we can work with python types
# same happens we receive JSON data, fast api converts it to python types for us to work with


'''Running the webserver  
>uvicorn main:app --reload
>uvicorn <python filename>:<fastapi object> --reload
reload is to autoreload on change
'''

@app.get("/about")
def about():
    return {"Data": "About"}

#path parameter and query parameter
inventory = {
    1: {
        "name":"Milk",
        "price":100,
        "brand":"Amul"
        },
    2: {
        "name":"Biscuits",
        "price":200,
        "brand":"Parle"
        }
}

#endpoint that can retrieve for us the item info from inventory based on its id
''' var : type name == type hing == type annotation
This tells that the item_id should be an int
'''
@app.get('/get-item/{item_id}')
def get_item(item_id : int ):
    return inventory[item_id]