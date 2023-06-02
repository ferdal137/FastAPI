from fastapi import FastAPI
from database import database as connection

#Start the server: uvicorn main:app

app = FastAPI(title = 'Project Movie Review',
            description = 'In this project we create a web app to share movie reviews',
            version = '1')

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

        print('Connecting...')

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

        print('Close')

@app.get('/')
async def index():
    return 'Hello world from fastAPI server'

