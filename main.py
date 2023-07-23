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
    return {"Data":"Test"}
#when we run our webserver and hit the root endpoint, it will return us the dictionary
