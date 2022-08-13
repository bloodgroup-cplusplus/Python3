FROM python:3.9

# organize the folders in containers in slightly better way 

# create working direcotry 

# this is our starting point
WORKDIR /fastapi-app


# we will copy requirements.txt inside the Workdir 

COPY requirements.txt .

RUN pip install -r rquirements.txt

COPY ./app ./dockerapp

CMD [ "python", "./main.py" ]



