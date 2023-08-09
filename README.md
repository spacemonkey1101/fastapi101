# Why FastAPI?

You can create an API fast(duh!). Apart from that.
 - [Data Validation] You define the type of all of the data that your API is expecting. You have to set the validations explicitly otherwise(traditionaly). Fastapi automatically sends you error messages in case of such errors
 - [Auto Documentation] Auto documents your entire API. Generates a webpage with this info
 - [Auto Completion and Code Suggestions] Better completion in IDEs as we are already defining types

## Pre-requisite:
- `pip install fastapi`
- `pip install uvicorn` (Uvicorn lets us run the API as a webserver)

## What is an Endpoint?

Point of entry in a communication channel when 2 systems are interacting
It is of the form baseURL/endpoint

### Examples:
- /hello
- /get-item
- localhost/form
  - localhost is the baseURL when we are hosting locally
- facebook.com/home


## What is an API?

Application Program Interface. Its a webservice that provides an interface to applications to manipulate and retrieve info.

Example: Amazon would have an API for managing inventory.
Any application(web, mobile) can talk to the same inventory API to get the details. So they can have a single backend for all of their different frontend.

### Path parameter is the parameter that comes in the URL path
Eg: amazon.com/bedcover/1

### Query paramenter is the parameter that comes in the URL path after a questsion mark '?'
Eg: facebook.com/home?redirect=/tim&msg=fail
So we set 2 parameters redirect and msg

### Request Body
Often times when we are trying to add info to a DB, we are not going to be sending info in query or path params.
We will send a bunch of info together in a request body