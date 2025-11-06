from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    gender: str

application = FastAPI()

def authenticate(request : Request):

    password = request.headers["Authorization"]
    if password != "Amruta@123":
        raise HTTPException(status_code = 404, detail = 'item not found' )

@application.get('/')
def root(_ : bool = Depends(authenticate)):
    return {"Amruta" : "pune"}

@application.get('/items/{item_id}')
def param(item_id : int):
    return {"Amruta" : "coder", "id" : item_id}

@application.get('/norm_para')
def norm_para(s: Person= Depends()):
    return {"name": s.name,
            "gender": s.gender
            }





