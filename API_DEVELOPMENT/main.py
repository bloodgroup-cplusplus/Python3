from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()

#this is called path operation
#the first component is the function and the second component is the decorateor
# the async is only written so that we can do all the tasks asynchronously
#the documentation choose the root
# the name is an arbitrary name
# make it descriptive
# if you are trying to login a user name it login
# we could perform any type of logic
# checking passwords in the database
# whatever we return is the data that is sent to the user
# we are written to dictionarly
# fast apis send it to json automatically
# we see it on the web browser

# decorators are turning it into a path operator
# we refrence our fast api refrence
# this is a get method and we want to use the get requst
# "/" is the root path . Basically the name of the api
# our web server
# google.com == google.com/
#/ is the path we have to go to in the URL
#/ posts/vote ( if changed it could change )

@app.get("/")
async def root():


    #anytime you change the code your server gets updated
    # anytime you want to update the fresh changes run pass the reload flag
    # uvicorn main:app --reload
    return {"message": "Welcome to my api "}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}

# if the two functions are same the fast api looks top down format
# FIFO method
# once we have to send data to api we need a frontend application
# there is a lot of differnt tools we have
# one of these tools is called postman
# postman for api testing


# with post request we can send data to our API server
# post requst with data on the api server
# and the api will send the api we want
# title content
# we send it to api server
# it can send back some data
# a get request is saying get some data
# a post requst is giveing data to api server

@app.post("/createposts")

def create_posts(payLoad:dict = Body(...)):
    #payload is the data we get from the Body ( frontend )

    print(payLoad)


#why we need schema
# It's a pain to get all the values from the body
# The client can send whatever data they want
# The data isn't getting validated
# We ultimately want to force the client to send data in a schema that we
# expect








