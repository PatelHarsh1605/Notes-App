from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schema.note import noteEntitey,notesEntitey
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_items(request: Request):

    docs = conn.NoteBook.NoteBook.find({})
    newDocs = []
    for doc in docs :
        newDocs.append({
            "id": str(doc["_id"]),
            "title" : doc["title"],
            "desc" : doc["desc"],
            "important" : doc["important"]
        })
    
    return  templates.TemplateResponse(
        name = "index.html",
        context = {"request" : request,"newDocs": newDocs}
    )


@note.post("/")
async def add_note(request : Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important")== "on" else False
    note = conn.NoteBook.NoteBook.insert_one(formDict)
    return {"Success":True}
    