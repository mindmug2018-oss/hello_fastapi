from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app=FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)

def home(request:Request):
    result = templates.TemplateResponse('index.html', {
    'request':request,
    'fortuneToday': 'You will meet your fated partner today!'
    })    
    return result

