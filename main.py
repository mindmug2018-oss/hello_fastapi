from fastapi import FastAPI, Request, Depends

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session



# Calling Database
DB_URL = "postgresql://scott:tiger@localhost/scott_db"
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app=FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)

def home(request:Request, db: Session = Depends(get_db)):
    query = text('''
        SELECT num, content
        FROM notice
        ORDER BY num DESC
    ''')
    result = db.execute(query)
    notice_list = result.fetchall()
    
    result2 = templates.TemplateResponse(
    {'request':request},
    name='index.html',
    context={
        'fortuneToday': 'You will meet your fated partner today!',
        "noticelist":notice_list
        }
    )    
    return result2

