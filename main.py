from fastapi import FastAPI

#creates an API object
app = FastAPI() 

'''
GET - endpoint that returns information
POST - sending/adding data to the enpoint
PUT , DELETE
'''
#setting up root GET endpoint
@app.get("/")
def home():
    return {"Data":"Testing"}
#when we run our webserver and hit the root endpoint, it will return us the dictionary
# as soon as the function returns the dictionary is converted to a JSON
# this is a easier way for HTTP traffic to exchange
# fastapi handles JSONifying all of our data, so that we can work with python types
# same happens we receive JSON data, fast api converts it to python types for us to work with


'''Running the webserver  
>uvicorn main:app --reload
>uvicorn <python filename>:<fastapi object> --reload
reload is to autoreload on change
'''