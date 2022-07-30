from fastapi import FastAPI


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



