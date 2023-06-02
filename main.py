from fastapi import FastAPI

app = FastAPI(title = 'Project Movie Review',
            description = 'In this project we create a web app to share movie reviews',
            version = '1')


@app.get('/')
async def index():
    return 'Hello world from fastAPI server'


@app.get('/about')
async def about():
    return 'About'