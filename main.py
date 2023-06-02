from fastapi import FastAPI

#Start the server: uvicorn main:app

app = FastAPI(title = 'Project Movie Review',
            description = 'In this project we create a web app to share movie reviews',
            version = '1')

@app.on_event('startup')
def startup():
    print('The server is starting')

@app.on_event('shutdown')
def shutdown():
    print("The server is ending")

@app.get('/')
async def index():
    return 'Hello world from fastAPI server'

